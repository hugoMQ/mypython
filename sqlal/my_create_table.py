#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 9:21
# @Author  : yuguo
#创建数据 库

# ORM中的数据表是什么呢?
# Object Relation Mapping
# Object - Table 通过 Object 去操纵数据表
# 从而引出了我们的第一步创建数据表 - 创建Object
# 1. 创建Object
# class User(object):
#     pass

# 2. 让Object与数据表产生某种关系 也就是让Object与数据表格式极度相似
# 导入官宣基础模型
from sqlalchemy.ext.declarative import declarative_base
# 实例化官宣模型 - Base 就是 ORM 模型
Base = declarative_base()
# 当前的这个Object继承了Base也就是代表了Object继承了ORM的模型
class User(Base):  # 相当于 Django Models中的 Model
    # 为Table创建名称
    __tablename__ = "user"
    # 创建ID数据字段 , 那么ID是不是一个数据列呢? 也就是说创建ID字段 == 创建ID数据列
    from sqlalchemy import Column,Integer,String
    # id = Column(数据类型,索引,主键,外键,等等)
    # int == Integer
    id = Column(Integer,primary_key=True,autoincrement=True)
    # str == char(长度) == String(长度)
    name = Column(String(32),index=True)

# 3.去数据库中创建数据表? or 先连接数据库?
# 3.去连接数据库 创建数据引擎
from sqlalchemy import create_engine
# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")

# Base 自动检索所有继承Base的ORM 对象 并且创建所有的数据表
Base.metadata.create_all(engine)



