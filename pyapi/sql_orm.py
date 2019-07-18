#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-17 14:21
# @Author  : yuguo
'''
sql orm 框架
1. /select后面跟用户
2. sql语句转化为orm框架
3. 异常返回值标准化处理，json
'''

import json
from flask import Flask, request
from pyapi.user import User, db_session
from pyapi.result import Result

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def userList():
    '''
    查询所有用户
    '''

    # ORM查询语句
    try:
        users = db_session.query(User).all()
    except Exception as e :
        return Result(error=f"查询失败，失败原因：{e}")
    if users == None:
        return Result(error="没有用户")
    para = []
    for row in users:
        user = {'id':row.id,'name':row.name,'age':row.age}
        para.append(user)
    # indent参数根据数据格式缩进显示
    # 输出真正的中文需要指定ensure_ascii=False
    return json.dumps(para, ensure_ascii=False)

@app.route('/selectId/<id>',methods=['GET'])
def findUserById(id):
    '''
    根据id查询用户
    '''
    if id == None:
        return Result(error="输入参数不可为空")
    try:
        user = db_session.query(User).filter(User.id == id).first()
    except Exception as e:
        return Result(error=f"查询失败，失败原因：{e}")
    if user == None:
        return Result(error="没有查询到用户")
#对象如何转换为json
    result = {'id': user.id, 'name': user.name, 'age': user.age}
    print(user.__dict__)
    return json.dumps(result,ensure_ascii=False)

@app.route('/selectName/<name>',methods=['GET'])
def findUserByName(name):
    '''
    根据name模糊查询用户

    '''
    if name == None or name.strip() == "":
        return Result(error="输入参数不可为空")
    print('=====================')
    print(name)                 #传入中文会乱码
    print('=====================')
    try:
        users = db_session.query(User).filter(User.name.like('%%%s%%' %name)).all()
        if len(users) == 0:
            return Result(error="没有查询到用户")
        para = []
        for row in users:
            user = {'id': row.id, 'name': row.name, 'age': row.age}
            para.append(user)
    except Exception as e:
        return Result(error=f"查询失败，失败原因：{e}")
    # indent参数根据数据格式缩进显示
    # 输出真正的中文需要指定ensure_ascii=False
    return json.dumps(para, ensure_ascii=False)

@app.route('/insert', methods=['POST'])
def addUser():
    '''
    添加用户
    '''
    json = request.json
    name=json.get("name").strip()
    age = json.get("age").strip()
    if name == "":
        return Result(error="用户姓名不可为空")
    if  age == "":
        return Result(error="用户年龄不可为空")
    user = User(name=name,age=age)
    try:
        db_session.add(user)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return Result(error=f"添加用户失败，失败原因：{e}")

    return Result(msg="用户添加成功")

@app.route('/delete/<id>', methods=['DELETE'])
def delUser(id):
    '''
    根据id删除用户 
    '''
    if id == None:
        return Result(error="输入参数不可为空")
    try:
        db_session.query(User).filter(User.id == id).delete()
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return Result(error=f"删除用户失败，失败原因：{e}")
    finally:
        db_session.close()
    return Result(msg="用户删除成功")


if __name__ == '__main__':
    #开启debug模式的好处在于，每次对源代码的修改，保存一下刷新页面都可以立即生效，而不用重启程序。
    app.run(host='127.0.0.1', port=5590,debug=True)