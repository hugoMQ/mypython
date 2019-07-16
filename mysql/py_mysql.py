#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 14:05
# @Author  : yuguo
# pymysql  语法，一般作为sqlalchemy的驱动使用
import pymysql
db = pymysql.connect(host="localhost",user="root",password="root",db="examination_system",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()


# 编写sql 查询语句  user 对应我的表名
sql = "select * from student"

try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("userID", "userName", "sex")
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
#
#

#插入操作
sql_insert = "insert into userlogin(userID,userName,password,role) values(10009,'hugu','123',2)"
try:

    cur.execute(sql_insert)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()

sql_update = "update userlogin set userName = '小王' where userID=23"
try:

    cur.execute(sql_update)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()


sql_delete = "delete from userlogin where userID = 23"
try:
    cur.execute(sql_delete)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()