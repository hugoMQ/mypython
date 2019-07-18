#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-17 14:26
# @Author  : yuguo
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
    # primary_key 主键
    #unique=True 此列不允许出现重复值
    #nullable=Tuue，此列允许使用空值，=False 此列不允许使用空值
    #default 为这列定义默认值
    #index=True 为这列创建索引，提升查询 效率
    name = Column(String(32),nullable=False,unique=True,index=True)
    age = Column(Integer,nullable=False)


# 3.去连接数据库 创建数据引擎
from sqlalchemy import create_engine
# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")

# Base 自动检索所有继承Base的ORM 对象 并且创建所有的数据表
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
db_session = Session()