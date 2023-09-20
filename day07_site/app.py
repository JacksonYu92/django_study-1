import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def db_execute(sql, arg_list):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='shanghai', passwd='root123', charset='utf8',
                           db='day07_site')
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute(sql, arg_list)
    conn.commit()

    cursor.close()
    conn.close()

def db_fetchall(sql, arg_list):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='shanghai', passwd='root123', charset='utf8',
                           db='day07_site')
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute(sql, arg_list)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
@app.route('/phone/list')
def phone_list():
    data_list = db_fetchall("select id,mobile,city,name from phone order by id desc", [])
    return render_template('phone_list.html', data_list=data_list)

@app.route('/add/phone')
def add_phone():
    mobile = request.args.get("mobile")
    city = request.args.get("city")
    user = request.args.get("user")

    db_execute("insert into phone(mobile,city,name)values(%s,%s,%s)", [mobile, city, user])

    return redirect("/phone/list")

@app.route('/delete/phone')
def delete_phone():
    pid = request.args.get("pid")

    db_execute("delete from phone where id=%s", [pid, ])

    return redirect("/phone/list")

if __name__ == '__main__':
    app.run()