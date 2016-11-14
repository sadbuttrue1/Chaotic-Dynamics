import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def f(µ, x):
    return µ * x * (-x + 1)


µs = [1., 2.8, 3.2, 3.58, 3.583, 4.]
x_0 = np.arange(0, 1.01, 0.01)

for µ in µs:
    x = np.empty((100, 101))
    x[0, :] = f(µ, x_0)
    plt.figure()
    for i in range(1, 100):
        x[i, :] = f(µ, x[i - 1, :])
        y = np.empty(101)
        y.fill(i)
        plt.plot(x[i, :], y, 'b.', markersize=2)
    plt.xlabel("x")
    plt.ylabel("k")
    plt.xlim([-0.1, 1.1])
    plt.ylim([0, 110])
    plt.savefig("mu={}.png".format(µ))
    x_test = x[99, :]
    # counts = dict(Counter(np.around(x_test, decimals=3)))
    # values = list(filter(lambda x: counts[x] > 6, counts.keys()))
    # print(µ)
    # print(counts)
    # print(list(filter(lambda x: counts[x] > 6, counts.keys())))
    # for v in values:
    #     for i in range(100):
    #         tmp = f(µ, v)
    #         if tmp == v:
    #             print('µ = {} value = {} order = {}'.format(µ, v, i))
    #             break
    for i in range(100):
        x_test = f(µ, x_test)
        if np.allclose(x_test, x[99, :], atol=1.e-4):
            print("µ = {} Order = {}".format(µ, i + 1))
            break
