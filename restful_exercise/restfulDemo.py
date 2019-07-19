#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 11:15
# @Author  : yuguo
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}



#API接口：Resource充当路由的角色
#Flask-RESTful 提供的最主要的基础就是资源(resources)
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
