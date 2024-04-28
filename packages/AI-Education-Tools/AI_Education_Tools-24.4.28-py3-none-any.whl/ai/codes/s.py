# 导入模块
import streamlit as st
import pandas as pd
import numpy as np

# 用户界面（UI）组件
st.title('Streamlit 应用示例')

# 数据处理
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# 应用逻辑
option = st.sidebar.selectbox('选择一个选项', ('显示数据', '显示统计信息'))

# 展示结果
if option == '显示数据':
    st.write('原始数据：', data)
elif option == '显示统计信息':
    st.write('数据统计信息：', data.describe())

# 添加交互组件
if st.checkbox('显示图表'):
    chart_type = st.selectbox('选择图表类型', ('折线图', '散点图'))
    if chart_type == '折线图':
        st.line_chart(data)
    elif chart_type == '散点图':
        st.scatter_chart(data)
