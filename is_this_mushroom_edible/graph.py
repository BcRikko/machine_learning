# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 採取したキノコのデータ
data = np.loadtxt("./data.txt", delimiter=" ")

# 食べたキノコのデータ
eaten = np.loadtxt("./eaten.txt", delimiter=" ")


# 散布図の作成
def plot(data, eaten):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # 採取したキノコの描画
    x1, y1 = np.array([[x[0], x[1]] for x in data]).T
    ax.scatter(x1, y1, color="b")

    # 食べたキノコの描画
    x2, y2 = np.array([[x[0], x[1]] for x in eaten if x[2] == 1]).T
    ax.scatter(x2, y2, color="r")

    # 毒キノコの描画
    x3, y3 = np.array([[x[0], x[1]] for x in eaten if x[2] == 0]).T
    ax.scatter(x3, y3, color="g")

    plt.legend(loc="best")
    plt.show()


plot(data, eaten)