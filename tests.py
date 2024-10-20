import math
from main import integrate


def f1(x):
    return math.sin(x)


def f2(x):
    return math.cos(2*x)


def f3(x):
    return math.tan(x)


def test_sinx():
    assert integrate(f1, 0, 5, n_iter=100) == 0.71618857


def test_cos2x():
    assert integrate(f2, 0, 7, n_iter=50) == 0.49206346


def test_small_tanx():
    assert integrate(f3, 0, 0.01, n_iter=10) == 0.00005000


if __name__ == '__main__':
    print("Error from test_sinx: ", test_sinx())
    print("Error from test_cos2x: ", test_cos2x())
    print("Error from test_small_tanx: ", test_small_tanx())
