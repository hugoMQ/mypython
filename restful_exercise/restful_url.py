#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 14:23
# @Author  : yuguo
'''
案例二(通过url里面的参数作为查询的参数)

（1）通过url传递参数，给视图函数，这种方式一般用在get请求，post请求通过form表单形式比较实用 
（2）通过url传递参数，需要定义函数时候，使用形参t_id,且在使用add_resource（）函数的使用，url参数形式最后添加变量，例如’/update_delete/’这个形式。 
（3）第三个函数delete这个函数，最终执行删除是成功的，但是最终并没有返回return的字符串”delete success”，具体原因不详，可能是用法不对，后续再更新中说明

'''

from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

Tasks = {
    't1': {'task': 'eat an app'},
    't2': {'task': 'play football'},
    't3': {'task': 'watching TV'},
}

#获取表单数据
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Tasks:
        abort(404, message="Todo {} doesn't exist".format(t_id))

class Update_Delete(Resource):
    # 根据t_id获取对应的value
    def get(self,t_id):
        abort_if_todo_doesnt_exist(t_id)
        return Tasks[t_id]
    # 根据t_id删除对应的value
    def delete(self,t_id):
        abort_if_todo_doesnt_exist(t_id)
        del Tasks[t_id]
        return "delete success", 204

    #判断t_id是否存在，并返回Tasks整个列表
    def post(self,t_id):
        abort_if_todo_doesnt_exist(t_id)
        return Tasks,200

    #根据t_id添加对应的value，并返回所有值
    def put(self,t_id):
        args = parser.parse_args()
        task = {"task":args['task']}
        Tasks[t_id] = task
        return Tasks,201

api.add_resource(Update_Delete,"/update_delete/<t_id>")

if __name__ == '__main__':
    app.run(debug=True)
