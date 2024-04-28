# 导入所需的库
from sklearn import datasets
import openml


# 获取iris数据集
iris = datasets.fetch_openml(name="iris", version=1)
print("Iris 数据集:")
print(iris.data.head())

# 获取wine数据集
wine = datasets.fetch_openml(name="wine", version=1)
print("\nWine 数据集:")
print(wine.data.head())

from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

# 示例数据矩阵
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 计算余弦相似度矩阵
cosine_similarity_matrix = pairwise_distances(X, metric='cosine')

print("余弦相似度矩阵:")
print(cosine_similarity_matrix) # 输出 0.974631846198

import pandas as pd

# 创建包含重复值和越界值的DataFrame
data = {'ID': [1, 2, 3,2 ,4, 5, 2],
        'Value': [10, 25, 30,25, 45, 5, 60]}

df = pd.DataFrame(data)

# 显示原始DataFrame
print("原始DataFrame:")
print(df)
print()

# 处理重复值
df_no_duplicates = df.drop_duplicates()

# 显示处理后的DataFrame（删除重复值）
print("处理重复值后的DataFrame:")
print(df_no_duplicates)
print()

# 处理越界值
lower_bound = 20
upper_bound = 50

# 替换越界值
df['Value'] = df['Value'].clip(lower=lower_bound, upper=upper_bound, inplace=False)
df['Value'] = df['Value'].mask(df['Value'] > upper_bound, lower_bound)

# 显示处理后的DataFrame（替换越界值）
print(f"替换越界值后的DataFrame:")
print(df)
