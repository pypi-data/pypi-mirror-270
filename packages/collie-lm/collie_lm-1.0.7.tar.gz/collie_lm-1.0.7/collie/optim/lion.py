import torch
from torch.optim.optimizer import Optimizer

__all__ = [
  "Lion"
]

class Lion(Optimizer):
  """
  一个优化器类Lion的官方实现。
  论文地址：https://arxiv.org/abs/2302.06675
  仓库地址：https://github.com/google/automl/blob/master/lion/lion_pytorch.py
  
  :param params: 待优化的参数
  :param lr: 学习率，默认值为1e-4，通常低于Adam使用的学习率
  :param betas: 用于计算运行时梯度均值和其平方的系数
  :param weight_decay：权重衰减系数，默认值为0.0
  """

  def __init__(self, params, lr=1e-4, betas=(0.9, 0.99), weight_decay=0.0):

    if not 0.0 <= lr:
      raise ValueError('Invalid learning rate: {}'.format(lr))
    if not 0.0 <= betas[0] < 1.0:
      raise ValueError('Invalid beta parameter at index 0: {}'.format(betas[0]))
    if not 0.0 <= betas[1] < 1.0:
      raise ValueError('Invalid beta parameter at index 1: {}'.format(betas[1]))
    defaults = dict(lr=lr, betas=betas, weight_decay=weight_decay)
    super().__init__(params, defaults)

  @torch.no_grad()
  def step(self, closure=None):
    loss = None
    if closure is not None:
      with torch.enable_grad():
        loss = closure()

    for group in self.param_groups:
      for p in group['params']:
        if p.grad is None:
          continue

        # Perform stepweight decay
        p.data.mul_(1 - group['lr'] * group['weight_decay'])

        grad = p.grad
        state = self.state[p]
        # State initialization
        if len(state) == 0:
          # Exponential moving average of gradient values
          state['exp_avg'] = torch.zeros_like(p)

        exp_avg = state['exp_avg']
        beta1, beta2 = group['betas']

        # Weight update
        update = exp_avg * beta1 + grad * (1 - beta1)
        p.add_(torch.sign(update), alpha=-group['lr'])
        # Decay the momentum running average coefficient
        exp_avg.mul_(beta2).add_(grad, alpha=1 - beta2)

    return loss