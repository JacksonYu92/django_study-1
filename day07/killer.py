import pymysql
from pymysql.cursors import DictCursor

username = input("用户名：")
password = input("密码：")
# age = input("年龄：")

# 1.连接
conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='root', charset='utf8', db='cmcc')
# cursor = conn.cursor()
cursor = conn.cursor(cursor=DictCursor)

# 2.执行SQL语句（指令）
# cursor.execute("insert into userinfo(user,pwd,age)values(%s,%s,%s);",[username,password,age])
# conn.commit()
cursor.execute("select * from userinfo where user=%s and pwd=%s", [username, password])
result = cursor.fetchone()
# print(result)

# 3.关闭连接
cursor.close()
conn.close()

if result:
    print("登录成功")
else:
    print("登录失败")