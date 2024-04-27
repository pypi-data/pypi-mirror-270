"""Provide gradietn descent optimizer"""

from typing import Literal

from .base import Optimizer, np
from .autograd import Tensor


class SGD(Optimizer):
    """
    Stochastic Gradient Descent optimizer.
    refer to https://pytorch.org/docs/stable/generated/torch.optim.SGD.html
    """

    def __init__(
        self,
        params: list[Tensor],
        lr: float = 0.001,
        momentum: float = 0,
        dampening: float = 0,
        weight_decay: float = 0,
        nesterov: bool = False,
        regularization: Literal[None, "l1", "l2"] = None,
        regular_strength: float = 1,
    ) -> None:
        super().__init__()
        self.params = params
        self.lr = lr
        self.momentum = momentum
        self.dampening = dampening
        self.weight_decay = weight_decay
        self.nesterov = nesterov
        self.regularization = regularization
        self.regular_strength = regular_strength
        self.step_now = 0

    def step(self):
        for param in self.params:
            x = param.data
            if self.regularization is None:
                g = param.grad / param.back_counter
            elif self.regularization == "l2":
                g = (
                    param.grad / param.back_counter
                    + self.regular_strength * 2 * param.data
                )
            elif self.regularization == "l1":
                g = param.grad / param.back_counter + self.regular_strength * np.sign(
                    param.data
                )
            else:
                raise ValueError("Invalid regularization method.")
            if self.weight_decay != 0:
                g = g + self.weight_decay * x
            if self.momentum != 0:
                # param.b is the momentum cache
                if self.step_now > 0:
                    param.b = self.momentum * param.b + (1 - self.dampening) * g
                else:
                    param.b = g
                if self.nesterov:
                    g = g + self.momentum * param.b
                else:
                    g = param.b
            # update
            param.data = x - self.lr * g
        self.step_now += 1


class Adam(Optimizer):
    """
    Adam optimizer is faster than SGD in most time.
    refer to
        https://pytorch.org/docs/stable/generated/torch.optim.Adam.html
    and
        https://arxiv.org/pdf/1412.6980.pdf
    """

    def __init__(
        self,
        params: list[Tensor],
        lr: float = 0.001,
        betas: list[float] = [0.9, 0.999],
        eps: float = 1e-8,
        weight_decay: float = 0,
        regularization: Literal[None, "l1", "l2"] = None,
        regular_strength: float = 0,
    ) -> None:
        super().__init__()
        self.params = params
        self.lr = lr
        self.betas = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.regularization = regularization
        self.regular_strength = regular_strength
        self.step_now = 0

    def step(self):
        for param in self.params:
            beta1, beta2 = self.betas
            x = param.data
            if self.regularization is None:
                g = param.grad / param.back_counter
            elif self.regularization == "l2":
                g = (
                    param.grad / param.back_counter
                    + self.regular_strength * 2 * param.data
                )
            elif self.regularization == "l1":
                g = param.grad / param.back_counter + self.regular_strength * np.sign(
                    param.data
                )
            else:
                raise ValueError("Invalid regularization method.")
            if self.weight_decay != 0:
                g = g + self.weight_decay * x
            if self.step_now > 0:
                # Update biased first moment estimate)
                param.m = beta1 * param.m + (1 - beta1) * g
                # Update biased second raw moment estimate
                param.v = beta2 * param.v + (1 - beta2) * g**2
            else:
                param.m = np.zeros_like(g)
                param.v = np.zeros_like(g)
            # Correct bias
            m = param.m / (1 - pow(beta1, self.step_now + 1))
            v = param.v / (1 - pow(beta2, self.step_now + 1))
            # update
            param.data = x - self.lr * m / (np.sqrt(v) + self.eps)
        self.step_now += 1


def test_Regression(sgd=False, iterations=10_000):
    """
    Test on Linear Regression problem, compared with scipy.optimize.lsq_linear

    find b to minimize `norm(y - y_hat)` where `y_hat = X @ b`

    """
    import scipy
    from .functional import Inner, Norm, Add

    np.random.seed(0)
    inner = Inner()
    add = Add()
    norm = Norm()
    rand = np.random.random
    SIZE = 3
    X = Tensor(rand((SIZE, SIZE)) * 2)
    beta = Tensor(rand(SIZE), requires_grad=True)
    y = Tensor(4 * (rand(SIZE) - 0.5))
    if sgd:
        optimizer = SGD(
            params=[beta],
            momentum=0.1,
            dampening=0.5,
            lr=0.001,
            weight_decay=0.01,
            regularization="l2",
            regular_strength=0.1,
        )
    else:
        optimizer = Adam(
            params=[beta],
            lr=0.01,
            weight_decay=0.01,
            regularization="l2",
            regular_strength=0,
        )
    for _ in range(iterations):
        loss = norm(add(inner(X, beta), -y))
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print("using", np.__name__)
    if np.__name__ == "cupy":
        res = scipy.optimize.lsq_linear(X.data.get(), y.data.get())
    elif np.__name__ == "numpy":
        res = scipy.optimize.lsq_linear(X.data, y.data)
    print(res.x, res.cost, res.status)
    print(beta.data, loss.data[0])


if __name__ == "__main__":
    print("SGD optimization")
    test_Regression(True, 10000)
    print("Adam optimization")
    test_Regression(False, 10000)
