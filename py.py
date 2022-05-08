import math
import numpy as np


class Cash(object):
    """Декоратор с кэшем для n последних вызовов функций

    Parameters
    ----------
    n : int
        размер кэша

    Attributes
    ----------
    cnt : int
        кол-во вызовов функции
    cash_size : int
        размер кэша
    cash : dict
        словарь размера cash_size в котором хранятся параметры и результат работы функции на этих параметрах

    """
    def __init__(self, n: int):
        self.cnt = 0
        self.cash = {}
        self.cash_size = n

    def __call__(self, fun):
        def wrapped_f(*args):
            # print(self.cash)
            if args not in self.cash:
                if len(self.cash) < self.cash_size:
                    self.cash[args] = [self.cnt % N, fun(*args)]
                else:
                    for key in self.cash.keys():
                        if self.cash[key][0] == (self.cnt - self.cash_size) % self.cash_size:
                            del self.cash[key]
                            break
                    self.cash[args] = [self.cnt % self.cash_size, fun(*args)]
                self.cnt += 1
            return self.cash[args][1]
        return wrapped_f


print(Cash.__doc__)
N = 2


@Cash(N)
def f1(a: int, b: int) -> int:
    return a * 1 + b


assert sum(f1(i, i + 1) for i in range(5)) == 25
N = 5


@Cash(N)
def f2(x: float) -> float:
    return math.sin(math.pi * x)


assert round(sum(f2(abs(i)) for i in np.arange(-2, 2.5, .5)), 16) == 0
