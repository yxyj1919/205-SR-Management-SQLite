import sqlite3
from datetime import datetime

class PreCheckDB:
    def __init__(self, conn):
        """
        初始化数据库检查类
        参数:
            conn: 数据库连接对象
        """
        self.conn = conn

    def check(self):
        """检查并初始化数据库"""
        try:
            cur = self.conn.cursor()
            
            # 创建表
            cur.execute('''
                CREATE TABLE IF NOT EXISTS srtable (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sr TEXT NOT NULL,
                    owner TEXT NOT NULL,
                    pr INTEGER,
                    comment TEXT,
                    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            ''')
            
            # 检查是否已有数据
            cur.execute('SELECT COUNT(*) FROM srtable')
            count = cur.fetchone()[0]
            
            # 如果表是空的，插入测试数据
            if count == 0:
                print('插入测试数据...')
                test_data = [
                    ('24012345678', '张工', 234567, 'Kubernetes集群扩容失败'),
                    ('24023456789', '李工', 345678, 'Docker容器无法启动'),
                    ('24034567890', '王工', 456789, '数据库备份异常'),
                    ('24045678901', '陈工', 567890, 'Jenkins构建失败'),
                    ('24056789012', '刘工', 678901, '网络连接超时'),
                    ('24067890123', '赵工', 789012, '日志系统异常'),
                    ('24078901234', '孙工', 890123, '内存使用率过高'),
                    ('24089012345', '周工', 901234, 'CPU负载异常'),
                ]
                
                cur.executemany('''
                    INSERT INTO srtable (sr, owner, pr, comment)
                    VALUES (?, ?, ?, ?)
                ''', test_data)
                
                print(f'成功插入{len(test_data)}条测试数据')
            
            self.conn.commit()
            cur.close()
            self.conn.close()
            
        except sqlite3.Error as e:
            print(f"数据库初始化错误: {e}")
            raise