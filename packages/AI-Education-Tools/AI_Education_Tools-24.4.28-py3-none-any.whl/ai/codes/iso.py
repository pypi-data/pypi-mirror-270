import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# 生成模拟购物数据，其中包含一些异常值
np.random.seed(42)
normal_data = np.random.normal(loc=100, scale=20, size=1000)
anomalies = np.random.normal(loc=300, scale=50, size=20)
shopping_data = np.concatenate([normal_data, anomalies])

# 将数据整理成一维数组
shopping_data = shopping_data.reshape(-1, 1)

# 使用孤立森林算法进行建模
clf = IsolationForest(contamination=0.05, random_state=42)  # contamination 表示异常值的比例
clf.fit(shopping_data)

# 预测异常值
predictions = clf.predict(shopping_data)

# 可视化结果
plt.scatter(range(len(shopping_data)), shopping_data, c=predictions, cmap='viridis')
plt.xlabel('Data Point Index')
plt.ylabel('Shopping Amount')
plt.title('Isolation Forest for Anomaly Detection')
plt.show()
