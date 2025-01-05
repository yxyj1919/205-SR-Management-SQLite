import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
from init_db import PreCheckDB

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_SERVER'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD')
        )
        return conn
    except psycopg2.Error as e:
        print(f"数据库连接错误: {e}")
        raise

PreCheckDB(get_db_connection()).check()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM srtable;')
    srtable = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', srs=srtable)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        sr_number = request.form['sr_number']
        sr_owner = request.form['sr_owner']
        pr_number = int(request.form['pr_number'])
        sr_comment = request.form['sr_comment']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO srtable (sr, owner, pr, comment)'
                    'VALUES (%s, %s, %s, %s)',
                    (sr_number, sr_owner, pr_number, sr_comment))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route("/delete/<int:id>")
def delete(id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE from srtable where id=%s", (id,))
                conn.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"删除记录时发生错误: {e}")
        return render_template("error.html", error=str(e))

@app.route("/modify/<int:id>")
def modify(id):
    conn = get_db_connection()
    cur = conn.cursor()
    # select row from booklist table for bookid passed from list page
    cur.execute("SELECT * FROM srtable where id="+str(id))
    sr = cur.fetchall()
    #display data in modify page passing the tuple as parameter in render_template method
    return render_template("modify.html",sr=sr )

@app.route("/update", methods=["POST"])
def update():
    #store values recieved from HTML form in local variables
    id=request.form.get("id")
    sr=request.form.get("sr")
    owner=request.form.get("owner")
    pr=request.form.get("pr")
    comment=request.form.get("comment")
    #create string update query with the values from form
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("update srtable set sr='"+sr+"', owner='"+owner+"',pr='"+pr+"', comment='" +comment+ "' where id="+str(id))
    #Execute update query
    #cur.execute(strSQl)
    #commit to database
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
# https://csveda.com/postgresql-flask-web-application-modify-and-delete-table-data/

@app.route('/about')
def about():
    return render_template('about.html',)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)