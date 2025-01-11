# 导入必要的模块
import sqlite3
from flask import Flask, render_template, request, url_for, redirect
from init_db import PreCheckDB
from datetime import datetime
import os
from config import Config

app = Flask(__name__)

def get_db_connection():
    """
    创建数据库连接
    返回: sqlite3连接对象，配置为可通过列名访问数据
    """
    try:
        # 确保数据库目录存在
        os.makedirs(Config.DATABASE_DIR, exist_ok=True)
        
        # 使用完整的数据库路径
        conn = sqlite3.connect(Config.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"数据库连接错误: {e}")
        raise

# 初始化数据库
def init_db():
    """初始化数据库"""
    PreCheckDB(get_db_connection()).check()

# 确保在应用启动时初始化数据库
init_db()

@app.route('/')
def index():
    """
    首页路由
    显示所有SR记录的列表
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM srtable;')
    srtable = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', srs=srtable)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    """
    创建新SR记录的路由
    GET: 显示创建表单
    POST: 处理表单提交，创建新记录
    """
    if request.method == 'POST':
        # 获取表单数据
        sr_number = request.form['sr_number']
        sr_owner = request.form['sr_owner']
        # 处理PR可能为空的情况
        pr_number = request.form['pr_number']
        pr_number = int(pr_number) if pr_number else None
        sr_comment = request.form['sr_comment']

        # 插入数据库
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO srtable (sr, owner, pr, comment)
            VALUES (?, ?, ?, ?)''',
            (sr_number, sr_owner, pr_number, sr_comment))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route("/delete/<int:id>")
def delete(id):
    """
    删除SR记录的路由
    参数:
        id: 要删除的记录ID
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE from srtable where id=?", (id,))
                conn.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"删除记录时发生错误: {e}")
        return render_template("error.html", error=str(e))

@app.route("/modify/<int:id>")
def modify(id):
    """
    修改SR记录的路由 - 显示修改表单
    参数:
        id: 要修改的记录ID
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM srtable WHERE id = ?", (id,))
    sr = cur.fetchall()
    return render_template("modify.html", sr=sr)

@app.route("/update", methods=["POST"])
def update():
    """
    更新SR记录的路由 - 处理修改表单的提交
    """
    # 获取表单数据
    id = request.form.get("id")
    sr = request.form.get("sr")
    owner = request.form.get("owner")
    # 处理PR可能为空的情况
    pr = request.form.get("pr")
    pr = int(pr) if pr else None
    comment = request.form.get("comment")
    
    # 更新数据库
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE srtable 
        SET sr = ?, owner = ?, pr = ?, comment = ? 
        WHERE id = ?""", 
        (sr, owner, pr, comment, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """关于页面路由"""
    return render_template('about.html')

@app.template_filter('datetime')
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    """格式化日期时间"""
    if value is None:
        return ""
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').strftime(format)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)