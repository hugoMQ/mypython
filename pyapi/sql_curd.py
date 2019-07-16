#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 20:27
# @Author  : yuguo

'''
实现用户管理(api接口的形式)
1. post方法添加用户
2. delete方法删除用户
3. get方法查询用户信息（模糊查询）
要求: 需要包含异常判断,前期可以先用pymysql实现
'''
import pymysql
import os
import json
from flask_cors import *
from flask import Flask, request

app = Flask(__name__)


@app.route('/select', methods=['GET'])
def findUser():
    arg = request.args.get('name')
    # 编写sql 查询语句
    if arg == None:
        sql_select = "select * from user "
    else:
         sql_select = "select * from user where name like '%%%s%%'" % (arg)
    db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 执行sql语句
    try:
        cur.execute(sql_select)
        # 获取查询的所有记录
        results = cur.fetchall()
    except Exception as e:
        return "查询失败"
    para = []
    for row in results:
        text = {'id':row[0],'name':row[1],'age':row[2]}
        para.append(text)
    return json.dumps(para, ensure_ascii=False, indent=4)

@app.route('/delete', methods=['DELETE'])
def delUser():
    # 获取输入数据
    name = request.args.get('name')
    if name == None:
        return "输入参数不可为空"
    db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 编写sql 查询语句  user 对应我的表名
    sql_delete = "delete from user where name='%s'"%(name)
    try:
        # 执行sql语句
        execute = cur.execute(sql_delete)
        db.commit()
    except Exception as e:
        db.rollback()
        return "删除失败"
    finally:
        db.close()
    return '删除成功'


@app.route('/insert', methods=['POST'])
def addUser():
    json = request.json
    name=json.get("name").strip()
    age = json.get("age").strip()
    if name == "" or age == "":
        return "输入参数不可为空"

    # 数据库连接
    db = pymysql.connect(host="localhost", user="root", password="root", db="mydb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 编写sql 查询语句
    sql_insert = "insert into user(name,age) values('%s','%s')"%(name,age)
    # 执行sql语句
    try:
        cur.execute(sql_insert)
        db.commit()
    except Exception as e:
        db.rollback()
        return " 插入失败"

    return '用户添加成功'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5590)