#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 11:47
# @Author  : yuguo

#Flask-RESTful 内置了支持验证请求数据

from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)


#获取 表单中的数据，放入parser中
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('name', type=str)

# 获取  &  更新
class Get_Modify(Resource):
    def get(self):
        args = parser.parse_args()
        print(args)
        return args, 200


api.add_resource(Get_Modify, '/get_modify')

if __name__ == '__main__':
    app.run(debug=True)
