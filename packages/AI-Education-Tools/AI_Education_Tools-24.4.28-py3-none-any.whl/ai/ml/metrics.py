from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
# 多组n维向量
X = np.array([[1, 2, 3], [4, 8,33], [117, 228, 339]])
# 计算多组向量之间的切比雪夫距离
d = pairwise_distances(X, metric='chebyshev')
print("切比雪夫距离矩阵：\n", d)

def bi_distances(X):
    t=['chebyshev', 'euclidean', 'manhattan']

distances_types={
    'manhattan':1,
    'euclidean':2,
    'chebyshev':np.inf,


}

from sklearn.metrics import pairwise_distances

# 生成两个示例数据集
X = [[0, 1], [1, 1]]
Y = [[1, 2], [2, 2]]

# 计算曼哈顿距离
distances_manhattan = pairwise_distances(X, Y, metric='minkowski', p=1)

# 计算欧几里德距离（默认）
distances_euclidean = pairwise_distances(X, Y, metric='minkowski', p=2)

print("Manhattan Distances:")
print(distances_manhattan)

print("\nEuclidean Distances:")
print(distances_euclidean)
print('*'*33)
d = pairwise_distances(X, Y, metric='minkowski', p=3)
print(d)
