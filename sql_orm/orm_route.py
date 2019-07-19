#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 9:07
# @Author  : yuguo


from pyapi.result import Result
from sql_orm.user import User,db   #此处不可循环调用
import  json
from flask import Blueprint,  request
#蓝图
##Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
userModel = Blueprint('userModel', __name__)


@userModel.route('/list', methods=['GET'])
def userList():
    '''
    查询所有用户
    '''

    # ORM查询语句
    try:
        users = User.query.all()
    except Exception as e :
        return Result(error=f"查询失败，失败原因：{e}")
    if users == None:
        return Result(error="没有用户")
    para = []
    for row in users:
        user = {'id':row.id,'name':row.name,'email':row.email}
        para.append(user)
    # indent参数根据数据格式缩进显示
    # 输出真正的中文需要指定ensure_ascii=False
    return json.dumps(para, ensure_ascii=False)

@userModel.route('/selectId/<id>',methods=['GET'])
def findUserById(id):
    '''
    根据id查询用户
    '''
    if id == None:
        return Result(error="输入参数不可为空")
    try:
        user = User.query.filter_by(id == id).first_or_404()
        print(user)
    except Exception as e:
        return Result(error=f"查询失败，失败原因：{e}")

    result = {'id': user.id, 'name': user.name, 'email': user.email}
    print(user.__dict__)
    return json.dumps(result,ensure_ascii=False)

@userModel.route('/selectName/<name>',methods=['GET'])
def findUserByName(name):
    '''
    根据name模糊查询用户

    '''
    if name == None or name.strip() == "":
        return Result(error="输入参数不可为空")
    try:
        users = User.query.filter(User.name.like('%%%s%%' %name)).all()
        if len(users) == 0:
            return Result(error="没有查询到用户")
        para = []
        for row in users:
            user = {'id': row.id, 'name': row.name, 'age': row.email}
            para.append(user)
    except Exception as e:
        return Result(error=f"查询失败，失败原因：{e}")
    # indent参数根据数据格式缩进显示
    # 输出真正的中文需要指定ensure_ascii=False
    return json.dumps(para, ensure_ascii=False)

@userModel.route('/insert', methods=['POST'])
def addUser():
    '''
    添加用户
    '''
    json = request.json
    name=json.get("name").strip()
    email = json.get("email").strip()
    pswd = json.get("pswd").strip()
    if name == "":
        return Result(error="用户姓名不可为空")
    if email == "":
        return Result(error="邮箱不可为空")
    user = User(name=name,email=email,pswd=pswd)
    print(user)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Result(error=f"添加用户失败，失败原因：{e}")

    return Result(msg="用户添加成功")

@userModel.route('/delete/<id>', methods=['DELETE'])
def delUser(id):
    '''
    根据id删除用户 
    '''
    if id == None:
        return Result(error="输入参数不可为空")
    try:
        User.query.filter(User.id == id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Result(error=f"删除用户失败，失败原因：{e}")
    finally:
        db.session.close()
    return Result(msg="用户删除成功")
