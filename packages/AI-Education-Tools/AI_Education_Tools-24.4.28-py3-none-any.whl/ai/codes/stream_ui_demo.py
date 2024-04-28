import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置页面标题
st.title("Streamlit UI 示例")

# 显示标题
st.header("这是一个标题")

# 显示子标题
st.subheader("这是一个子标题")

# 显示文本内容
st.write("这是一段文本内容。")

# 文本输入框
user_input_text = st.text_input("请输入您的文本：", "")

# 数字输入框
user_input_number = st.number_input("请输入一个数字：", min_value=0, max_value=100, step=1)

# 下拉选择框
options = ["苹果", "香蕉", "橘子"]
selected_option = st.selectbox("请选择一个选项：", options)

# 单选按钮
radio_options = ["男", "女"]
selected_radio_option = st.radio("请选择您的性别：", radio_options)

# 多选框
multiselect_options = ["红色", "蓝色", "绿色"]
selected_multiselect_options = st.multiselect("请选择颜色：", multiselect_options)

# 滑动条
slider_value = st.slider("选择一个范围：", min_value=0, max_value=100, value=(25, 75))

# 按钮
button_clicked = st.button("点击这里")

# 图片显示
image = plt.imread("Streamlit.png")
st.image(image, caption="示例图片", use_column_width=True)

# 使用Matplotlib绘制折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot()

# 显示用户输入的内容
st.write("您输入的文本是：", user_input_text)
st.write("您输入的数字是：", user_input_number)
st.write("您选择的选项是：", selected_option)
st.write("您选择的性别是：", selected_radio_option)
st.write("您选择的颜色是：", selected_multiselect_options)
st.write("您选择的范围是：", slider_value)
st.write("按钮是否被点击：", button_clicked)
