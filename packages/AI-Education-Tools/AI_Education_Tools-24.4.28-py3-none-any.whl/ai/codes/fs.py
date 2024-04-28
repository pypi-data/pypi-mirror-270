import flwr as fl

# 启动 Flower 服务器
def main():
    # 配置服务器设置
    server = fl.server.Server(config={"num_rounds": 3})
    server.start()

if __name__ == "__main__":
    import os

  # 设置 PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION 环境变量为 python
    os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
    main()