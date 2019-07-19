#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 11:31
# @Author  : yuguo

#在资源路由上（resources）定义多个方法（get，post，put等），就可以实现多种效果

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
