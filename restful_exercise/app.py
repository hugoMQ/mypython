#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 9:35
# @Author  : yuguo
from flask import Flask
from restful_exercise.login import loginModule

app = Flask(__name__)

app.register_blueprint(loginModule, url_prefix='/loginModule')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
