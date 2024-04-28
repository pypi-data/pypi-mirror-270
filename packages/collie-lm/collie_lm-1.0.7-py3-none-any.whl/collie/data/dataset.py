"""CoLLie 中预定义的数据结构
"""
import io
import json
import mmap
import os
import random
import threading
from functools import reduce
from typing import Dict, List, Optional, Sequence, Tuple, Callable

import numpy as np
import torch
from torch.utils.data import Dataset
from torch.utils.data.dataset import Dataset
from transformers import PreTrainedTokenizer

from collie.driver.io import FileIODriver
from .template_utils import tokenize_conversation

__all__ = [
    "CollieDatasetForTraining",
    "CollieDatasetForTemplatedMultiTurnChat",
    "CollieDatasetForGeneration",
    "CollieDatasetForClassification",
]


class _ShardContainer(list):
    def __init__(self, path, shuffle: bool = False, seed: int = 1024) -> None:
        list.__init__([])
        self.file = None
        self.file_name = None
        self.shuffle = shuffle
        self.seed = seed
        self.threadlocal = threading.local()
        meta_files = []
        for file in FileIODriver.list(path):
            if file.endswith(".meta"):
                meta_files.append(os.path.join(path, file))
        self.meta = [
            [
                {"file": file, "offset": meta[0], "length": meta[1]}
                for meta in FileIODriver.load(file, mode="rb")
            ]
            for file in meta_files
        ]
        self.meta = np.hstack(self.meta).tolist()
        self.indices = list(range(len(self.meta)))
        if self.shuffle:
            random.seed(self.seed)
            random.shuffle(self.indices)

    def _get_mmap(self, path):
        if not hasattr(self.threadlocal, "handles"):
            with open(path, "rb") as f:
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                self.threadlocal.handles = [f, mm]
                if (
                        path.endswith(".gz")
                        or path.endswith(".bz")
                        or path.endswith(".bz2")
                ):
                    raise NotImplementedError(
                        "Compressed files are not supported because .seek() would require "
                        "rereading the entire file, making performance too slow."
                    )
        return self.threadlocal.handles[-1]

    def __len__(self):
        return len(self.meta)

    def __getitem__(self, index):
        meta = self.meta[self.indices[index]]
        file_name: str = meta["file"]
        if (
                self.file is None
                or self.file_name != file_name.replace(".meta", "")
                or (isinstance(self.file, mmap.mmap) and self.file.closed)
        ):
            self.file_name = file_name.replace(".meta", "")
            if self.file is not None:
                self.file.close()
            self.file = self._get_mmap(self.file_name)
        self.file.seek(meta["offset"])
        return json.loads(self.file.readline().decode())


def _inspect_special_tokens_length(tokenizer):
    ids_with_special_tokens = tokenizer("a", add_special_tokens=True).input_ids
    ids_without_special_tokens = tokenizer("a", add_special_tokens=False).input_ids
    bos_length = 0
    for bos_length in range(len(ids_with_special_tokens)):
        if ids_with_special_tokens[bos_length] == ids_without_special_tokens[0]:
            break
    eos_length = (
            len(ids_with_special_tokens) - len(ids_without_special_tokens) - bos_length
    )
    return bos_length, eos_length


class CollieDatasetForTraining(Dataset):
    """**CoLLie** 中的基本数据格式，可用于预训练、微调任务。
    需提供的dataset数据格式形似：

    .. code-block::

        [
            {
                "text": "这是prompt部分的文本",
            },
            ...
        ]

    或者:

    .. code-block::

        [
            {
                "input": "这是prompt部分的文本",
                "output": "这是output部分的文本"
            },
            ...
        ]

    或者:

    .. code-block::

        [
            {
                "tokens": [token_id_1, token_id_2, ...],
                "labels": [-100, token_id_2, ...] # 可选，-100 表示计算 loss 时忽略该 token
            },
            ...
        ]

    当使用第二种数据格式时，只有 `output` 部分的 token 会参与 loss计算。
    当使用第二种数据格式时，`labels` 字段是可选的，如果不提供 `labels` 默认计算所有 token 的 loss
    """

    def __init__(
            self,
            dataset: Sequence[Dict],
            tokenizer: Optional[PreTrainedTokenizer] = None,
            add_special_tokens: bool = True,
            shuffle: bool = False,
            seed: int = 1024,
            max_length: int = -1,
    ):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.add_special_tokens = add_special_tokens
        self.indices = list(range(len(self.dataset)))
        self.max_length = max_length
        if shuffle:
            random.seed(seed)
            random.shuffle(self.indices)
        if self.tokenizer is not None:
            self.bos_length, self.eos_length = _inspect_special_tokens_length(self.tokenizer)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index) -> Dict or List[Dict]:
        if isinstance(index, slice):
            return self._get_slice(index)
        if index > len(self):
            raise IndexError("Index out of range.")
        index = self.indices[index]
        if self.tokenizer is None:
            if isinstance(self.dataset[index]["tokens"], torch.Tensor):
                self.dataset[index]["tokens"] = self.dataset[index]["tokens"].numpy().tolist()
            if isinstance(self.dataset[index]["labels"], torch.Tensor):
                self.dataset[index]["labels"] = self.dataset[index]["labels"].numpy().tolist()
            input_ids = self.dataset[index]["tokens"]
            labels = self.dataset[index].get("labels", input_ids.copy())
            if "attention_mask" in self.dataset[index].keys():
                attention_mask = self.dataset[index]["attention_mask"]
            else:
                attention_mask = [1 for _ in range(len(input_ids))]
        else:
            if "text" in self.dataset[0].keys():
                inputs = self.tokenizer(
                    self.dataset[index]["text"],
                    add_special_tokens=self.add_special_tokens,
                )
                input_ids = inputs["input_ids"]
                labels = torch.tensor(input_ids).cpu().tolist()
                attention_mask = inputs.get(
                    "attention_mask",
                    [1 for _ in range(len(input_ids))],
                )
            elif (
                    "input" in self.dataset[0].keys() and "output" in self.dataset[0].keys()
            ):
                inputs = self.tokenizer(
                    self.dataset[index]["input"] + self.dataset[index]["output"],
                    add_special_tokens=self.add_special_tokens,
                )
                input_ids = inputs["input_ids"]
                attention_mask = inputs.get(
                    "attention_mask",
                    [1 for _ in range(len(input_ids))],
                )
                labels = torch.tensor(input_ids)
                target_length = len(
                    self.tokenizer(
                        self.dataset[index]["output"],
                        add_special_tokens=self.add_special_tokens,
                    ).input_ids
                )
                if self.add_special_tokens:
                    target_length -= self.bos_length
                labels[: -target_length] = -100
                labels = labels.cpu().tolist()
            else:
                raise ValueError("Dataset must have one or two fields.")
        if self.max_length > 0:
            input_ids = input_ids[: self.max_length]
            attention_mask = attention_mask[: self.max_length]
            labels = labels[: self.max_length]
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels,
        }

    def _get_slice(self, s: slice):
        result = []
        for idx in self.indices[s]:
            result.append(self[idx])
        return result

    @classmethod
    def from_json(
            cls,
            path: str,
            tokenizer: Optional[PreTrainedTokenizer] = None,
            shuffle: bool = False,
            seed: int = 1024,
    ):
        dataset = cls(
            dataset=json.loads(FileIODriver.load(path, mode="r")),
            shuffle=shuffle,
            seed=seed,
            tokenizer=tokenizer,
        )
        return dataset

    @classmethod
    def from_processed(cls, path: str, shuffle: bool = False, seed: int = 1024):
        dataset = cls(dataset=_ShardContainer(path), shuffle=shuffle, seed=seed)
        return dataset

    def save_processed(self, path: str, shard_size: int = 4):
        shard = io.BytesIO()
        shard_idx = 0
        meta = np.empty((0, 2), int)
        for i in self.indices:
            data = {"tokens": self[i]["input_ids"]}
            data.update(
                {key: value for key, value in self[i].items() if key != "input_ids"}
            )
            bytes_data = json.dumps(data).encode() + "\n".encode()
            offset = shard.tell()
            length = len(data["tokens"])
            shard.write(bytes_data)
            meta = np.append(meta, np.array([[offset, length]]), axis=0)
            if shard.tell() > shard_size * 1024 * 1024 or i == len(self) - 1:
                file = f"collie-dataset-shard-{shard_idx}.bin"
                shard.seek(0)
                FileIODriver.save(meta, os.path.join(path, file + ".meta"))
                FileIODriver.save(shard.read().decode(), os.path.join(path, file))
                shard.close()
                shard = io.BytesIO()
                meta = np.empty((0, 2), int)
                shard_idx += 1


class CollieDatasetForPerplexity(CollieDatasetForTraining):
    ...


class CollieDatasetForTemplatedMultiTurnChat(CollieDatasetForTraining):
    """**CoLLie** 中的多轮对话数据集，会根据模板进行处理
    :param dataset: 提供的多轮对话数据，形如：

    .. code-block::

            [
                {
                    "history": [
                        {
                            "role": "user",
                            "content": "这是用户的问题"
                        },
                        {
                            "role": "assistant",
                            "content": "这是助手的回答"
                        },
                        ...
                    ]
                },
                ...
            ]

    :tokenizer: 用于处理数据的 tokenizer
    :shuffle: 是否打乱数据
    :seed: 随机种子
    :max_length: 每条数据最大长度
    :template_fn: 模板函数，为多轮对话数据添加模板
    :add_generation_prompt: 是否添加用于生成的 prompt，训练时不需要
    :text_field: 对话数据中文本字段的名称，默认为 `history`
    """
    def __init__(
            self,
            dataset: Sequence[Dict],
            tokenizer: Optional[PreTrainedTokenizer],
            shuffle: bool = False,
            seed: int = 1024,
            max_length: int = -1,
            template_fn: Optional[Callable] = None,
            add_generation_prompt: bool = False,
            text_field: str = "history",
    ):
        super().__init__(
            dataset=dataset,
            tokenizer=tokenizer,
            shuffle=shuffle,
            seed=seed,
            max_length=max_length,
        )
        self.template_fn = template_fn
        self.add_generation_prompt = add_generation_prompt
        self.text_field = text_field

    def __getitem__(self, index) -> Dict:
        if index > len(self):
            raise IndexError("Index out of range in dataset.")

        input_ids, labels, attention_mask = tokenize_conversation(
            self.dataset[index],
            self.tokenizer,
            text_field=self.text_field,
            prepare_template_fn=self.template_fn,
            add_generation_prompt=self.add_generation_prompt,
        )
        if self.max_length > 0:
            input_ids = input_ids[: self.max_length]
            attention_mask = attention_mask[: self.max_length]
            labels = labels[: self.max_length]
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels,
        }


class CollieDatasetForGeneration(CollieDatasetForTraining):
    """**CoLLie** 中的生成数据集，主要用于数据生成或者与生成相关的检验
    须搭配 :class:`~collie.controller.evaluator.EvaluatorForGeneration` 使用。需提供的数据格式形似:

        .. code-block::

            [
                {
                    "text": "这是prompt部分的文本",
                    "target": "目标文本" # 需要计算 bleu, rouge 值时需要加上这个字段
                },
                ...
            ]
    """

    def __getitem__(self, index) -> Dict:
        if index > len(self):
            raise IndexError("Index out of range.")
        target = None
        index = self.indices[index]
        if self.tokenizer is None:
            input_ids = self.dataset[index]["tokens"]
            if "attention_mask" in self.dataset[index].keys():
                attention_mask = self.dataset[index]["attention_mask"]
            else:
                attention_mask = [1 for _ in range(len(input_ids))]
            target = self.dataset[index].get("target", None)
        else:
            inputs = self.tokenizer(
                self.dataset[index]["text"], add_special_tokens=self.add_special_tokens
            )
            input_ids = inputs["input_ids"]
            attention_mask = inputs.get(
                "attention_mask",
                [1 for _ in range(len(input_ids))],
            )
            if "target" in self.dataset[index].keys():
                if isinstance(self.dataset[index]["target"], str):
                    target = [self.tokenizer(self.dataset[index]["target"]).input_ids]
                elif isinstance(self.dataset[index]["target"], (list, tuple, set)):
                    target = [
                        self.tokenizer(x).input_ids
                        for x in self.dataset[index]["target"]
                    ]
        if self.max_length > 0:
            input_ids = input_ids[: self.max_length]
            attention_mask = attention_mask[: self.max_length]
        sample = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": input_ids,
        }
        if target is not None:
            sample["target"] = target
        return sample


class CollieDatasetForClassification(CollieDatasetForTraining):
    """**CoLLie** 中的分类任务数据集
    须搭配 :class:`~collie.controller.evaluator.EvaluatorForClassfication` 使用。需提供的数据格式形似:

        .. code-block::

            [
                {
                    "input": "这是prompt部分的文本",
                    "output": ["类别1", "类别2", "类别3"],
                    "target": 0
                },
                ...
            ]
    """

    def __init__(
            self,
            dataset: Sequence[Dict],
            tokenizer: Optional[PreTrainedTokenizer] = None,
            add_special_tokens: bool = True,
            shuffle: bool = False,
            seed: int = 1024,
            max_length: int = -1,
            style: str = "harness",
    ):
        super().__init__(
            dataset=dataset,
            tokenizer=tokenizer,
            add_special_tokens=add_special_tokens,
            shuffle=shuffle,
            seed=seed,
            max_length=max_length,
        )
        assert style.lower() in (
            "harness",
            "helm",
        ), "Style can only be one of `harness` or `helm`"
        self.style = style.lower()

    def __getitem__(self, index) -> Dict:
        if index > len(self):
            raise IndexError("Index out of range.")
        index = self.indices[index]
        if self.tokenizer is None:
            input_ids = tuple(self.dataset[index]["tokens"])
            target = self.dataset[index]["target"]
        else:
            if self.style == "harness":
                if (
                        "input" in self.dataset[0].keys()
                        and "output" in self.dataset[0].keys()
                        and "target" in self.dataset[0].keys()
                ):
                    input_ids = []
                    attention_mask = []
                    labels = []
                    for output in self.dataset[index]["output"]:
                        inputs = self.tokenizer(
                            self.dataset[index]["input"] + output,
                            add_special_tokens=self.add_special_tokens,
                        )
                        input_ids.append(inputs.get("input_ids"))
                        attention_mask.append(
                            inputs.get(
                                "attention_mask",
                                torch.ones_like(torch.tensor(inputs.get("input_ids"))),
                            )
                        )
                        label = torch.tensor(inputs.get("input_ids"))
                        target_length = len(
                            self.tokenizer(
                                output,
                                add_special_tokens=self.add_special_tokens,
                            ).input_ids
                        )
                        if self.add_special_tokens:
                            target_length -= self.bos_length
                        label[: -target_length] = -100
                        label = label.cpu().tolist()
                        labels.append(label)

                    input_ids = tuple(input_ids)
                    labels = tuple(labels)
                    attention_mask = tuple(attention_mask)
                    target = self.dataset[index]["target"]
                else:
                    raise ValueError(
                        "CollieDatasetForClassification must have three fields (`input`, `output` and `target`)."
                    )
                if self.max_length > 1:
                    input_ids = [sample[: self.max_length] for sample in input_ids]
                    labels = [sample[: self.max_length] for sample in labels]
                    attention_mask = [
                        sample[: self.max_length] for sample in attention_mask
                    ]
                return {
                    "input_ids": input_ids,
                    "attention_mask": attention_mask,
                    "labels": labels,
                    "target": target,
                }
            elif self.style == "helm":
                if (
                        "input" in self.dataset[0].keys()
                        and "output" in self.dataset[0].keys()
                        and "target" in self.dataset[0].keys()
                ):
                    inputs = self.tokenizer(
                        self.dataset[index]["input"],
                        add_special_tokens=self.add_special_tokens,
                    )
                    input_ids = inputs["input_ids"]
                    attention_mask = inputs.get(
                        "attention_mask",
                        [1 for _ in range(len(input_ids))],
                    )
                    output = tuple([option for option in self.dataset[index]["output"]])
                    target = self.dataset[index]["target"]
                else:
                    raise ValueError(
                        "CollieDatasetForClassification must have three fields (`input`, `output` and `target`)."
                    )
                if self.max_length > 0:
                    input_ids = input_ids[: self.max_length]
                    attention_mask = attention_mask[: self.max_length]
                return {
                    "input_ids": input_ids,
                    "attention_mask": attention_mask,
                    "labels": input_ids,
                    "target": target,
                    "output": output,
                }
            else:
                raise ValueError("Style can only be one of `harness` or `helm`")
