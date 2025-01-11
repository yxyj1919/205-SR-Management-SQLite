# SR Management System

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

## 安装和运行

1. 克隆仓库
```bash
git clone https://github.com/你的用户名/仓库名.git
cd 仓库名
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python app.py
```

## 项目结构
```
project_root/
├── app.py              # 主应用文件
├── config.py           # 配置文件
├── init_db.py          # 数据库初始化文件
├── requirements.txt    # 项目依赖
├── static/            # 静态文件
│   └── style.css
└── templates/         # 模板文件
    ├── base.html
    ├── create.html
    └── index.html
\\\

## License

MIT
