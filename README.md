# SR Management System
![](https://yxyj1919-imagebed.oss-cn-beijing.aliyuncs.com/rocket-image/202501111529063.png)
一个基于Flask和SQLite的SR（Service Request）管理系统。

## 功能特点

- SR记录的增删改查
- 支持PR号关联
- 自动记录创建时间
- 响应式界面设计

## 技术栈

- Python
- Flask
- SQLite
- Bootstrap 5
- Docker

## 安装和运行

### 方式一：Docker 部署（推荐）

1. 构建 Docker 镜像
```bash
docker build -t sr-tracker .
```

2. 运行容器
```bash
docker run -d -p 5000:5000 -v $(pwd)/database:/app/database sr-tracker
```

参数说明：
- `-d`: 在后台运行容器
- `-p 5000:5000`: 将容器的 5000 端口映射到主机的 5000 端口
- `-v $(pwd)/database:/app/database`: 挂载数据库目录以持久化数据

3. 访问应用
打开浏览器访问 `http://localhost:5000`

### Docker 常用命令

```bash
# 查看运行中的容器
docker ps

# 停止容器
docker stop <container_id>

# 重启容器
docker restart <container_id>

# 查看容器日志
docker logs <container_id>
```

### 方式二：本地部署

1. 克隆仓库
```bash
git clone https://github.com/yxyj1919/205-SR-Management-SQLite.git
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python app.py
# 如果端口被占用
python app.py --port=5001
```

## 项目结构
```
project_root/
├── app.py              # 主应用文件
├── config.py           # 配置文件
├── init_db.py          # 数据库初始化文件
├── requirements.txt    # 项目依赖
├── Dockerfile          # Docker 配置文件
├── static/            # 静态文件
│   └── style.css
└── templates/         # 模板文件
    ├── base.html
    ├── create.html
    └── index.html
```

## License

MIT
