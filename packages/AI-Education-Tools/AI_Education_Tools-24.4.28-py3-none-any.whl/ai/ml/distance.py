from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
# 多组n维向量
X = np.array([[1, 2, 3], [4, 8,33], [117, 228, 339]])
# 计算多组向量之间的切比雪夫距离
d = pairwise_distances(X, metric='chebyshev')
print("切比雪夫距离矩阵：\n", d)

import numpy as np
from sklearn.metrics import pairwise_distances

# 生成两个示例数据集

# 计算 Chebyshev 距离（无穷大阶数）
distances_chebyshev = pairwise_distances(X,  metric='minkowski', p=np.inf)

print("Chebyshev Distances:")
print(distances_chebyshev)
