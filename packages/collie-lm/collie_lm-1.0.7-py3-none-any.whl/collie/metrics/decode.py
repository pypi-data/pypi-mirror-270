from typing import Any, Dict
from collie.metrics.base import BaseMetric
from collie.utils import env
from collie.log.logger import logger
import torch

class DecodeMetric(BaseMetric):
    """
    用以保存并打印 decode 生成内容的 metric

    :param verbose: 控制是否使用 logger 打印生成的 sentences
    :param save_to_file: 控制是否保存生成的 sentences 到文件夹中。
    :param save_path: 保存 decode 生成的 sentences 的文件路径, 当 save_to_file 为 `True` 才生效
    """
    def __init__(self, 
                 verbose: bool = True,
                 save_to_file: bool = False,
                 save_path: str = None,
                 gather_result: bool = True) -> None:
        super().__init__(gather_result)
        self.verbose = verbose
        self.save_to_file = save_to_file
        self.save_path = save_path
    
    def get_metric(self):
        """
        该 metric 不需要返回
        """
        return None

    def update(self, result: Dict):
        """
        :meth:`update` 函数将针对一个批次的预测结果做评价指标的累计。
        """
        assert "pred" in result, "result must contain key `pred`"
        # generated_ids = result['generated_ids']
        # decode_list = []
        # for i in range(len(generated_ids)):
        #     if isinstance(generated_ids[i], torch.Tensor):
        #         if generated_ids[i].ndim == 2:
        #             decode_list.extend(list(map(lambda x: x.detach().cpu().tolist(), [*generated_ids[i]])))
        #         else:
        #             decode_list.append(generated_ids[i].detach().cpu().tolist())
        #     else:
        #         decode_list.append(generated_ids[i])
        # sentences = []
        # for ids in decode_list:
        #     sentences.append(self.tokenizer.decode(ids))
        if (env.dp_rank == 0 or self.gather_result) and env.pp_rank == 0 and env.tp_rank == 0:
            if self.verbose:
                logger.info(result["pred"])
            if self.save_to_file:
                with open(self.save_path, 'a+') as f:
                    f.write('\n'.join(result["pred"]) + '\n')
