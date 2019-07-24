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
from flask_restful import Api
from sql_restful.orm_restful import Restful_Model



#设置连接数据库的URL
app.config.from_object('config')

#restful接口
api = Api(app)

#路由
api.add_resource(Restful_Model,'/users/<string:arg>')
# api.add_resource(Restful_Model,'/insert')
# api.add_resource(Restful_Model,'/delete/<id>')

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080,debug=True)