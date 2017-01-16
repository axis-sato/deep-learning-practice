import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    """
    ステップ関数
    :param np.array x : 入力
    """
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    """
    シグモイド関数
    :param np.array x : 入力
    """
    return 1 / (1 + np.exp(-x))


def relu(x):
    """
    ReLU関数
    :param np.array x : 入力
    """
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# y = sigmoid(x)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

