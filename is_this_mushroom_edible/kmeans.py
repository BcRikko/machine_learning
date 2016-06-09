# coding: utf-8

import numpy as np
from sklearn.cluster import KMeans

# 採取したキノコのデータ
data = np.loadtxt("./data.txt", delimiter=" ")

# 食べたキノコのデータ
eaten = np.loadtxt("./eaten.txt", delimiter=" ")

# KMeansでクラスタリング
def kmeans(feature):
    kmeans_model = KMeans(n_clusters=3, random_state=10).fit(feature)
    labels = kmeans_model.labels_
    return labels

labels = kmeans(data)

# 結果出力
features = []
for label, feature in zip(labels, data):
    if label == 0:
        # 食べてもいいキノコ
        features.append(feature)
        print(label, feature)

np.savetxt('./answer.txt', features)