import pymysql
from pymysql.cursors import DictCursor

# 连接MySQL（socket）
conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='root', charset='utf8', db='day07')
# cursor = conn.cursor()
cursor = conn.cursor(cursor=DictCursor)

# 1.查看数据库
# cursor.execute("show databases;")
# result = cursor.fetchall()
# print(result)

# 2.删除数据库
# cursor.execute("drop database gx_day15;")
# conn.commit()

# 3.进入数据库
# cursor.execute("use blog;")
# cursor.execute("show tables;")
# result = cursor.fetchall()
# print(result)

# 4.创建数据库
# cursor.execute("create database day08 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;")
# conn.commit()

# 1.创建表
# sql = """
# create table tb6(
# 	id int not null auto_increment primary key,
#     name varchar(16) not null,
#     email varchar(32) null,
#     age int default 3
# )default charset=utf8;
# """
# cursor.execute(sql)
# conn.commit()

# 2.删除表

# cursor.execute("drop table tb6;")
# conn.commit()

# 3. 清空表
# cursor.execute("delete from tb5;")
# conn.commit()


# 1.新增数据
# cursor.execute("insert into tb5(name,email,age) values('Jackson','xx', 19);")
# conn.commit()

# 2.删除
# cursor.execute("delete from tb5 where id=11;")
# conn.commit()

# 3.更新
# cursor.execute("update tb5 set age=20 where id>7;")
# conn.commit()

# 4.查询
cursor.execute("select * from tb5;")
data_list = cursor.fetchone()
# data_list = cursor.fetchall()
print(data_list)


cursor.close()
conn.close()