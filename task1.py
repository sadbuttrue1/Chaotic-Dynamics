import numpy as np


def f(µ, x):
    return µ * x * (1 - x)


µs = [1, 2.8, 3.2, 3.58, 3.583, 4]

for µ in µs:
    x_0 = np.arange(0, 1, 0.01)
    x = np.empty((100, 100))
    x[0, :] = x_0
    for i in range(1, 100):
        x[i, :] = f(µ, x[i - 1, :])
