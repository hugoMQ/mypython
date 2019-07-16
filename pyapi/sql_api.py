#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 16:42
# @Author  : yuguo
# -*- coding: UTF-8 -*-
import pymysql
import os
import json
from flask_cors import *
from flask import Flask, request

app = Flask(__name__)


@app.route('/select', methods=['GET'])
def findUser():
    arg = request.args.get('name')

    print(arg)
    # 数据库连接
    db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 编写sql 查询语句  user 对应我的表名
    #sql_select = "select * from user where name like %s" % ('%'+arg+'%')

    sql_select = "select * from user where name like '%%%s%%'" % (arg)

    #print(sql_select) select * from user where name like '%小%'
    # 执行sql语句
    cur.execute(sql_select)
    # 获取查询的所有记录
    results = cur.fetchall()
    print(request)
    para = []
    for row in results:
        text = {'id':row[0],'name':row[1],'age':row[2]}
        print(text)
        para.append(text)
    return json.dumps(para, ensure_ascii=False, indent=4)

@app.route('/delete', methods=['DELETE'])
def delUser():
    # 获取输入数据
    name = request.args.get('name')
    print(name)
    try:
        db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        # 编写sql 查询语句  user 对应我的表名
        sql_delete = "delete from user where name='%s'"%(name)
        #print(sql_delete) delete from user where name='小发'
        # 执行sql语句
        execute = cur.execute(sql_delete)
        print(execute)
        db.commit()
    except Exception as e:
        print(e)
        print('出现异常')
        db.rollback()
    finally:
        db.close()
    return 'success'


@app.route('/insert', methods=['POST'])
def addUser():
    json = request.json
    print(json)
    name=json.get("name")
    print(name)
    age = json.get("age")
    print(age)
    # 数据库连接
    db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 编写sql 查询语句  user 对应我的表名
    sql_insert = "insert into user(name,age) values('%s','%s')"%(name,age)
    #print(sql_insert) insert into user(name,age) values('小二','5')
    # 执行sql语句
    cur.execute(sql_insert)
    db.commit()

    return 'add success'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5590)