#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-17 10:03
# @Author  : yuguo
# coding:utf-8
# 一个基于Flask和SQLAlchemy+SQLite的极简博客应用
from sqlalchemy.ext.declarative import declarative_base
import json
import pymysql
from flask import Flask, request,render_template,redirect
from sqlalchemy.orm import sessionmaker
# 实例化官宣模型 - Base 就是 ORM 模型
Base = declarative_base()

# 创建应用程序对象
app = Flask(__name__)

from sqlalchemy import create_engine
# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")

# Base 自动检索所有继承Base的ORM 对象 并且创建所有的数据表
Base.metadata.create_all(engine)

class Blog(Base):  # 相当于 Django Models中的 Model
    # 为Table创建名称
    __tablename__ = "blog"
    # 创建ID数据字段 , 那么ID是不是一个数据列呢? 也就是说创建ID字段 == 创建ID数据列
    from sqlalchemy import Column,Integer,String
    # id = Column(数据类型,索引,主键,外键,等等)
    # int == Integer
    id = Column(Integer,primary_key=True,autoincrement=True)
    # str == char(长度) == String(长度)
    title = Column(String(32),index=True)
    text = Column(String(32),index=True)


@app.route('/')
def home():
    '''
    主页
    '''
    # 渲染首页HTML模板文件
    return render_template('home.html')

@app.route('/blogs/create', methods=['GET', 'POST'])
def create_blog():
    '''
    创建博客文章
    '''
    if request.method == 'GET':
        # 如果是GET请求，则渲染创建页面
        return render_template('create_blog.html')
    else:
        # 从表单请求体中获取请求数据
        title = request.form['title']
        text = request.form['text']

        # 创建一个博文对象
        blog = Blog(title=title, text=text)
        Session = sessionmaker(engine)
        # 打开会话对象 Session
        db_session = Session()
        #添加操作
        db_session.add(blog)
        # 必须提交才能生效
        db_session.commit()
        # 创建完成之后重定向到博文列表页面
        return redirect('/blogs')

@app.route('/blogs',methods = ['GET'])
def list_notes():
    '''
    查询博文列表
    '''
    Session = sessionmaker(engine)
    # 打开会话对象 Session
    db_session = Session()
    blogs = db_session.query(Blog).all()

    # 渲染博文列表页面目标文件，传入blogs参数
    return render_template('list_blogs.html',blogs = blogs)

@app.route('/blogs/<id>',methods = ['GET','DELETE'])
def query_note(id):
    '''
    查询博文详情、删除博文
    '''
    Session = sessionmaker(engine)
    # 打开会话对象 Session
    db_session = Session()
    if request.method == 'GET':
        print('get')
        # 到数据库查询博文详情
        blog = db_session.query(Blog).filter(Blog.id==id).first()
        # 渲染博文详情页面
        return render_template('query_blog.html',blog = blog)
    else:
        print('delete')
        # 删除博文
        blog = db_session.query(Blog).filter(Blog.id==id).delete()
        # 提交才能生效
        db_session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return '',204


@app.route('/blogs/update/<id>', methods=['GET', 'POST'])
def update_note(id):
    '''
    更新博文
    '''
    Session = sessionmaker(engine)
    # 打开会话对象 Session
    db_session = Session()
    if request.method == 'GET':

        # 根据ID查询博文详情
        blog = db_session.query(Blog).filter(Blog.id==id).first()
        # 渲染修改笔记页面HTML模板
        return render_template('update_blog.html', blog=blog)
    else:
        # 获取请求的博文标题和正文
        title = request.form['title']
        text = request.form['text']

        # 更新博文
        blog = db_session.query(Blog).filter(Blog.id==id).update({'title': title, 'text': text})
        # 提交才能生效
        db_session.commit()
        # 修改完成之后重定向到博文详情页面
        return redirect('/blogs/{id}'.format(id=id))

if __name__ == '__main__':
    # 以debug模式启动程序
    app.run(debug=True)