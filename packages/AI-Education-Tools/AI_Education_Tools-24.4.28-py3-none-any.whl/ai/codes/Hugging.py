import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Streamlit 页面设置
st.title("GPT-2 文本生成")

# 用户输入文本
input_text = st.text_area("请输入文本", "你的输入文本")

# 选择模型
model_name = st.selectbox("选择模型", ["gpt2", "your-custom-model-name"])
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 将文本编码为模型可接受的格式
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 获取模型输出
max_length = st.slider("选择生成文本的最大长度", 10, 200, 50)
num_beams = st.slider("选择束搜索数", 1, 10, 5)
no_repeat_ngram_size = st.slider("选择禁止重复的 n-gram 大小", 1, 5, 2)
output = model.generate(input_ids, max_length=max_length, num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size)

# 解码生成的文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# 显示生成的文本
st.subheader("生成的文本")
st.write(generated_text)
