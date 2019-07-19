#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-18 21:35
# @Author  : yuguo
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from pyapi.result import Result
from sql_orm.orm_route import userModel
from sql_orm.user import app

#注册蓝图，第一个参数logins是蓝图对象，
#url_prefix参数默认值是根路由，如果指定，会在蓝图注册的路由url中添加前缀。
app.register_blueprint(userModel)

#设置连接数据库的URL
app.config.from_object('config')
'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/Flask_test'

#设置每次请求结束后会自动提交数据中的更改，官方不推荐设置
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#如果一旦在数据库中把表结构修改，那么在sqlalchemy中的模型类也进行修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
'''
# db = SQLAlchemy(app)

# class Role(db.Model):
#     # 定义表名
#     __tablename__ = 'roles'
#     # 定义列对象
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     us = db.relationship('User', backref='role')
#
#     #repr()方法显示一个可读字符串
#     def __repr__(self):
#         return 'Role:%s'% self.name

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True, index=True)
#     email = db.Column(db.String(64),unique=True)
#     pswd = db.Column(db.String(64))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return 'User:%s'%self.name


# @app.route('/list', methods=['GET'])
# def userList():
#     '''
#     查询所有用户
#     '''
#
#     # ORM查询语句
#     try:
#         users = User.query.all()
#     except Exception as e :
#         return Result(error=f"查询失败，失败原因：{e}")
#     if users == None:
#         return Result(error="没有用户")
#     para = []
#     for row in users:
#         user = {'id':row.id,'name':row.name,'email':row.email}
#         para.append(user)
#     # indent参数根据数据格式缩进显示
#     # 输出真正的中文需要指定ensure_ascii=False
#     return json.dumps(para, ensure_ascii=False)
#
# @app.route('/selectId/<id>',methods=['GET'])
# def findUserById(id):
#     '''
#     根据id查询用户
#     '''
#     if id == None:
#         return Result(error="输入参数不可为空")
#     try:
#         user = User.query.filter_by(id == id).first_or_404()
#         print(user)
#     except Exception as e:
#         return Result(error=f"查询失败，失败原因：{e}")
#
#     result = {'id': user.id, 'name': user.name, 'email': user.email}
#     print(user.__dict__)
#     return json.dumps(result,ensure_ascii=False)
#
# @app.route('/selectName/<name>',methods=['GET'])
# def findUserByName(name):
#     '''
#     根据name模糊查询用户
#
#     '''
#     if name == None or name.strip() == "":
#         return Result(error="输入参数不可为空")
#     try:
#         users = User.query.filter(User.name.like('%%%s%%' %name)).all()
#         if len(users) == 0:
#             return Result(error="没有查询到用户")
#         para = []
#         for row in users:
#             user = {'id': row.id, 'name': row.name, 'age': row.email}
#             para.append(user)
#     except Exception as e:
#         return Result(error=f"查询失败，失败原因：{e}")
#     # indent参数根据数据格式缩进显示
#     # 输出真正的中文需要指定ensure_ascii=False
#     return json.dumps(para, ensure_ascii=False)
#
# @app.route('/insert', methods=['POST'])
# def addUser():
#     '''
#     添加用户
#     '''
#     json = request.json
#     name=json.get("name").strip()
#     email = json.get("email").strip()
#     pswd = json.get("pswd").strip()
#     if name == "":
#         return Result(error="用户姓名不可为空")
#     if email == "":
#         return Result(error="邮箱不可为空")
#     user = User(name=name,email=email,pswd=pswd)
#     print(user)
#     try:
#         db.session.add(user)
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         return Result(error=f"添加用户失败，失败原因：{e}")
#
#     return Result(msg="用户添加成功")
#
# @app.route('/delete/<id>', methods=['DELETE'])
# def delUser(id):
#     '''
#     根据id删除用户
#     '''
#     if id == None:
#         return Result(error="输入参数不可为空")
#     try:
#         User.query.filter(User.id == id).delete()
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         return Result(error=f"删除用户失败，失败原因：{e}")
#     finally:
#         db.session.close()
#     return Result(msg="用户删除成功")





if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # ro1 = Role(name='admin')
    # ro2 = Role(name='user')
    #
    # db.session.add_all([ro1,ro2])
    # db.session.commit()
    # us1 = User(name='wang',email='wang@163.com',pswd='123456',role_id=ro1.id)
    # us2 = User(name='zhang',email='zhang@189.com',pswd='201512',role_id=ro2.id)
    # us3 = User(name='chen',email='chen@126.com',pswd='987654',role_id=ro2.id)
    # us4 = User(name='zhou',email='zhou@163.com',pswd='456789',role_id=ro1.id)
    # db.session.add_all([us1,us2,us3,us4])
    # db.session.commit()
    app.run(host='127.0.0.1', port=8080,debug=True)