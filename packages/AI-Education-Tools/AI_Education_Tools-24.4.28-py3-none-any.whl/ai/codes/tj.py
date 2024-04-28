from PIL import Image, ImageDraw

# 创建新的图像，白色背景，尺寸为300x300
image = Image.new('RGB', (300, 300), color='white')

# 创建绘图对象
draw = ImageDraw.Draw(image)

# 绘制大圆
draw.ellipse((50, 50, 250, 250), fill='black', outline='black')

# 绘制小圆
draw.ellipse((50, 50, 250, 150), fill='white', outline='black')
draw.ellipse((50, 150, 250, 250), fill='black', outline='black')

# 绘制阴阳鱼
draw.pieslice((50, 50, 250, 150), start=90, end=270, fill='white', outline='black')  # 白色扇形
draw.pieslice((50, 150, 250, 250), start=-90, end=90, fill='black', outline='black')  # 黑色扇形

# 绘制鱼眼
draw.ellipse((120, 75, 180, 135), fill='white', outline='black')  # 白色眼眶
draw.ellipse((120, 165, 180, 225), fill='black', outline='black')  # 黑色眼眶

# 显示图像
image.show()

# 保存图像文件
image.save('taichi.png')
