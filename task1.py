import numpy as np
import matplotlib.pyplot as plt


def f(µ, x):
    return µ * x * (1 - x)


µs = [1., 2.8, 3.2, 3.58, 3.583, 4.]

for µ in µs:
    x_0 = np.arange(0, 1, 0.01)
    x = np.empty((101, 100))
    x[0, :] = x_0
    for i in range(1, 101):
        x[i, :] = f(µ, x[i - 1, :])
    plt.figure()
    plt.plot(x[:, 10], range(101))
    plt.xlabel("x")
    plt.ylabel("k")
    plt.savefig("mu={}.png".format(µ))
    x_test = x[100, :]
    for i in range(100):
        x_test = f(µ, x_test)
        if np.allclose(x_test, x[100, :], atol=1.e-4):
            print("µ = {} Order = {}".format(µ, i + 1))
            break
