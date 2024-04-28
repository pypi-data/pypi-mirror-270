import functools
from abc import ABC
from typing import Any, Callable, Dict, Optional, Union

from .callback import Callback
from .utils import _get_monitor_value
from collie.log import logger
from collie.utils import apply_to_collection
from collie.utils.utils import _check_valid_parameters_number

__all__ = ['HasMonitorCallback', 'ResultsMonitor']


class CanItemDataType(ABC):

    @classmethod
    def __subclasshook__(cls, subclass: Any) -> Union[bool, Any]:
        if cls is CanItemDataType:
            item = getattr(subclass, 'item', None)
            return callable(item)
        return NotImplemented


class ResultsMonitor:
    r"""监控某个数值并评估结果是否有所改善的监视器。

    可用于监控某个数值，并通过 :meth:`is_better_results` 等接口检测结果是否变得
    更好。

    :param monitor: 监控的 metric 值。

        * 为 ``None`` 时，不设置监控值。
        * 为 ``str`` 时，
          CoLLiE 将尝试直接使用该名称从 ``evaluation`` 的结果中寻找，如果最终在
          ``evaluation`` 结果中没有找到完全一致的名称，则将使用最长公共字符串算法
          从 ``evaluation`` 结果中找到最匹配的那个作为 ``monitor``。
        * 为 :class:`Callable` 时，
          则接受参数为 ``evaluation`` 的结果（字典类型），返回一个 ``float`` 值作
          为 ``monitor`` 的结果，如果当前结果中没有相关的 ``monitor`` 值则返回
          ``None``。
    :param larger_better: monitor 是否为越大越好；
    """

    def __init__(self,
                 monitor: Optional[Union[str, Callable]],
                 larger_better: bool = True):
        self.set_monitor(monitor, larger_better)
        self._log_name = self.__class__.__name__

    def set_monitor(self, monitor, larger_better):
        if callable(monitor):  # 检查是否能够接受一个参数
            _check_valid_parameters_number(
                monitor, expected_params=['results'], fn_name='monitor')
            self.monitor = monitor
        else:
            self.monitor = str(monitor) if monitor is not None else None
        if self.monitor is not None:
            self.larger_better = bool(larger_better)
        if larger_better:
            self.monitor_value = float('-inf')
        else:
            self.monitor_value = float('inf')
        self._real_monitor = self.monitor

    def itemize_results(self, results):
        r"""执行结果中所有对象的 :meth:`item` 方法（如果没有则忽略），使得 Tensor
        类型的数据转为 python 内置类型。

        :param results:
        :return:
        """
        return apply_to_collection(
            results, dtype=CanItemDataType, function=lambda x: x.item())

    def get_monitor_value(self, results: Dict) -> Union[float, None]:
        r"""获取 monitor 的值，如果 monitor 没有直接找到，会尝试使用 **最长公共字符
        串算法** 匹配的方式寻找。

        :param results: 评测结果；
        :return: monitor 的值；如果为 ``None``，表明此次没有找到合适的monitor；
        """
        if len(results) == 0 or self.monitor is None:
            return None
        # 保证所有的 tensor 都被转换为了 python 特定的类型
        results = self.itemize_results(results)
        use_monitor, monitor_value = _get_monitor_value(
            monitor=self.monitor, real_monitor=self._real_monitor, res=results)
        if monitor_value is None:
            return monitor_value
        # 第一次运行
        if isinstance(self.monitor, str) and \
                self._real_monitor == self.monitor and \
                use_monitor != self.monitor:
            logger.rank_zero_warning(
                f'We can not find monitor:`{self.monitor}` for '
                f'`{self.log_name}` in the evaluation result (with keys as '
                f'{list(results.keys())}), we use the `{use_monitor}` as the '
                'monitor.',
                once=True)
        # 检测到此次和上次不同。
        elif isinstance(self.monitor, str) and \
                self._real_monitor != self.monitor and \
                use_monitor != self._real_monitor:
            logger.rank_zero_warning(
                f'Change of monitor detected for `{self.log_name}`. '
                f'The expected monitor is:`{self.monitor}`, '
                f'last used monitor is:`{self._real_monitor}` '
                f'and current monitor is:`{use_monitor}`. '
                'Please consider using a customized monitor function when the '
                'evaluation results are varying between validation.')

        self._real_monitor = use_monitor
        return monitor_value

    def is_better_monitor_value(self,
                                monitor_value: float,
                                keep_if_better=True):
        """检测 ``monitor_value`` 是否是更好的。

        :param monitor_value: 待检查的 ``monitor_value``。如果为 ``None``，返
            回 False；
        :param keep_if_better: 如果传入的 ``monitor_value`` 值更好，则将其保存下
            来；
        :return:
        """
        if monitor_value is None:
            return False
        better = self.is_former_monitor_value_better(monitor_value,
                                                     self.monitor_value)
        if keep_if_better and better:
            self.monitor_value = monitor_value
        return better

    def is_better_results(self, results, keep_if_better=True):
        r"""检测给定的 ``results`` 是否比上一次更好，如果本次 results 中没有找到相
        关的 monitor 返回``False``。

        :param results: evaluation 结果；
        :param keep_if_better: 如果传入的 ``monitor_value`` 值更好，则将其保存下
            来；
        :return:
        """
        monitor_value = self.get_monitor_value(results)
        if monitor_value is None:
            return False
        return self.is_better_monitor_value(
            monitor_value, keep_if_better=keep_if_better)

    def is_former_monitor_value_better(self, monitor_value1, monitor_value2):
        """传入的两个值中，是否 ``monitor_value1`` 的结果更好。

        :param monitor_value1:
        :param monitor_value2:
        :return:
        """
        if monitor_value1 is None and monitor_value2 is None:
            return True
        if monitor_value1 is None:
            return False
        if monitor_value2 is None:
            return True
        better = False
        if (self.larger_better and monitor_value1 > monitor_value2) or \
                (not self.larger_better and monitor_value1 < monitor_value2):
            better = True
        return better

    @property
    def monitor_name(self):
        r"""返回 monitor 的名字，如果 monitor 是个 Callable 的函数，则返回该函数的
        名称。

        :return:
        """
        if callable(self.monitor):
            try:
                monitor = self.monitor
                while isinstance(monitor, functools.partial):
                    monitor = monitor.func
                monitor_name = monitor.__qualname__
            except Exception:
                monitor_name = self.monitor.__name__
        elif self.monitor is None:
            return None
        else:
            # 这里是能是monitor，而不能是real_monitor，因为用户再次运行的时候
            # real_monitor被初始化为monitor了
            monitor_name = str(self.monitor)
        return monitor_name

    @property
    def log_name(self) -> str:
        """内部用于打印当前类别信息使用。

        :return:
        """
        return self._log_name

    @log_name.setter
    def log_name(self, value):
        self._log_name = value


class HasMonitorCallback(ResultsMonitor, Callback):
    r"""对特定数值进行监控的 ``Callback``。

    该 callback 不直接使用，作为其它相关 callback 的父类使用，如果 callback
    有使用 monitor 可以继承该 ``Callback``。其已经实现了下面的功能：

    1. 判断 monitor 合法性；
    2. 在需要时，根据 trainer 的 monitor 设置自己的 monitor 名称。

    :param monitor: 监控的 metric 值：

        * 为 ``None`` 时，不设置监控值。
        * 为 ``str`` 时，
          CoLLiE 将尝试直接使用该名称从 ``evaluation`` 的结果中寻找，如果最终在
          ``evaluation`` 结果中没有找到完全一致的名称，则将使用最长公共字符串算法
          从 ``evaluation`` 结果中找到最匹配的那个作为 ``monitor``。
        * 为 :class:`Callable` 时，
          则接受参数为 ``evaluation`` 的结果（字典类型），返回一个 ``float`` 值作
          为 ``monitor`` 的结果，如果当前结果中没有相关的 ``monitor`` 值则返回
          ``None``。
    :param larger_better: monitor 是否为越大越好；
    :param must_have_monitor: 这个 callback 是否必须有 monitor 设置。如果设置为
        ``True``，且没检测到设置 monitor 会报错；
    """

    def __init__(self, monitor, larger_better, must_have_monitor=False):
        super().__init__(monitor, larger_better)
        self.must_have_monitor = must_have_monitor

    def on_after_trainer_initialized(self, trainer):
        r"""对于必须要有 monitor 设置的 callback ，该函数会进行检查。

        :param trainer:
        :return:
        """
        if self.must_have_monitor and self.monitor is None:
            raise RuntimeError(
                f'No `monitor` is set for {self.log_name}. '
                f'You can set it in the initialization or through Trainer.')
