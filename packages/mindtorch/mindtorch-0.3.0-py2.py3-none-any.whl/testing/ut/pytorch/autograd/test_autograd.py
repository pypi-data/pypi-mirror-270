import copy
from mindtorch import torch
from mindtorch.torch import nn
from ...utils import set_mode_by_env_config, enable_backward, SKIP_ENV_GRAPH_MODE

set_mode_by_env_config()

class Function(nn.Module):
    def __init__(self):
        super(Function, self).__init__()
        self.Linear = nn.Linear(1, 1)

    def forward(self, input):
        output = self.Linear(input)
        return output


@SKIP_ENV_GRAPH_MODE(reason="backward is not support graph mode now.")
def test_normal_train():
    with enable_backward():
        x = torch.tensor([2.0])
        y = torch.tensor([4.0])
        func = Function()
        loss_fn = nn.MSELoss()
        optim = torch.optim.SGD(func.parameters(), lr=0.01)

        w_grad_list = []
        for _ in range(3):
            optim.zero_grad()
            y_hat = func(x)
            loss = loss_fn(y_hat, y)
            loss.backward()
            # optim.step() each step different if update parameter
            w_grad_list.append(copy.deepcopy(func.Linear.weight.grad))

        assert w_grad_list[1].numpy() == w_grad_list[0].numpy()
        assert w_grad_list[2].numpy() == w_grad_list[0].numpy()


@SKIP_ENV_GRAPH_MODE(reason="backward is not support graph mode now.")
def test_grad_accumulate():
    with enable_backward():
        x = torch.tensor([2.0])
        y = torch.tensor([4.0])
        func = Function()
        loss_fn = torch.nn.MSELoss()
        optim = torch.optim.SGD(func.parameters(), lr=0.01)

        w_grad_list = []
        optim.zero_grad()
        for _ in range(3):
            y_hat = func(copy.deepcopy(x))
            loss = loss_fn(y_hat, y)
            loss.backward()
            w_grad_list.append(copy.deepcopy(func.Linear.weight.grad))

        optim.step()

        assert w_grad_list[1].numpy() == (2 * w_grad_list[0].numpy())
        assert w_grad_list[2].numpy() == (3 * w_grad_list[0].numpy())


def test_intermediate_values():
    with enable_backward():
        func = Function()
        x = torch.tensor([1.0])
        y = func(x)
        y_hat = y ** 2

        y_hat.backward()
        assert y.grad is None
        assert y_hat.grad is None


@SKIP_ENV_GRAPH_MODE(reason="backward is not support graph mode now.")
def test_joint_loss():
    with enable_backward():
        x = torch.tensor([2.0])
        y0 = torch.tensor([4.0])
        y1 = torch.tensor([4.0])
        func = Function()
        loss_fn = torch.nn.MSELoss()

        y_hat = func(copy.deepcopy(x))
        assert func.Linear.weight.grad is None
        loss0 = loss_fn(y_hat, y0)
        loss1 = loss_fn(y_hat, y1)
        (loss1 + loss0).backward()
        assert func.Linear.weight.grad is not None


@SKIP_ENV_GRAPH_MODE(reason="backward is not support graph mode now.")
def test_two_net_connect_with_detach():
    with enable_backward():
        x = torch.tensor([1.0])
        y = torch.tensor([2.0])

        func_0 = Function()
        func_1 = Function()
        loss_fn = torch.nn.MSELoss()

        y_0 = func_0(x)
        y_0 = y_0.detach()
        y_1 = func_1(y_0)
        loss = loss_fn(y_1, y)
        loss.backward()

        assert func_0.Linear.weight.grad is None
        assert func_0.Linear.bias.grad is None

        assert func_1.Linear.weight.grad is not None
        assert func_1.Linear.bias.grad is not None


@SKIP_ENV_GRAPH_MODE(reason="backward is not support graph mode now.")
def test_two_net_connect_without_detach():
    with enable_backward():
        x = torch.tensor([1.0])
        y = torch.tensor([2.0])

        func_0 = Function()
        func_1 = Function()
        loss_fn = torch.nn.MSELoss()

        y_0 = func_0(x)
        y_1 = func_1(y_0)
        loss = loss_fn(y_1, y)
        loss.backward()

        assert func_0.Linear.weight.grad is not None
        assert func_0.Linear.bias.grad is not None

        assert func_1.Linear.weight.grad is not None
        assert func_1.Linear.bias.grad is not None


def test_vanilla_backward():
    with enable_backward():
        x = torch.tensor([1.0], requires_grad=True)
        y = x * 2
        z = y + x
        z.backward()

        assert x.grad is not None
        assert x.grad.numpy() == [3]


if __name__ == '__main__':
    set_mode_by_env_config()
    test_normal_train()
    test_grad_accumulate()
    test_intermediate_values()
    test_joint_loss()
    test_two_net_connect_with_detach()
    test_two_net_connect_without_detach()
    test_vanilla_backward()