# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用程序代码
COPY . .

# 创建数据库目录
RUN mkdir -p /app/database

# 暴露端口
EXPOSE 5000

# 启动应用
CMD ["flask", "run", "--host=0.0.0.0"] 