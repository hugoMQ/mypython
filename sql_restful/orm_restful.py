#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-24 9:31
# @Author  : yuguo


import json

from flask import request
from flask_restful import Resource

from pyapi.result import Result
from sql_orm.user import User, db

class Restful_Model(Resource):

    def get(self,arg):
        '''
        根据name模糊查询用户
        '''
        name = arg
        if name == None or name.strip() == "":
            return Result(error="输入参数不可为空")
        try:
            users = User.query.filter(User.name.like('%%%s%%' % name)).all()
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
    #
    # @userModel.route('/insert', methods=['POST'])
    def post(self):
        '''
        添加用户
        '''
        json = request.json
        name = json.get("name").strip()
        email = json.get("email").strip()
        pswd = json.get("pswd").strip()
        if name == "":
            return Result(error="用户姓名不可为空")
        if email == "":
            return Result(error="邮箱不可为空")
        user = User(name=name, email=email, pswd=pswd)
        print(user)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return Result(error=f"添加用户失败，失败原因：{e}")

        return Result(msg="用户添加成功")
    #
    # @userModel.route('/delete/<id>', methods=['DELETE'])
    def delete(self,arg):
        '''
        根据id删除用户
        '''
        id = arg
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
