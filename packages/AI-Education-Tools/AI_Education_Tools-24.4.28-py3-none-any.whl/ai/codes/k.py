from transformers import GPT2Tokenizer, GPT2LMHeadModel

# 加载预训练的 GPT-2 模型和分词器
tokenizer = GPT2Tokenizer.from_pretrained("gpt ")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 输入文本
input_text = "He loves python"

# 将文本编码为模型可接受的格式
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 获取模型输出
output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2)

# 解码生成的文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
