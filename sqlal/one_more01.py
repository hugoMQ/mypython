#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 14:14
# @Author  : yuguo
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 这次我们要多导入一个 ForeignKey 字段了,外键关联对了
from sqlalchemy import Column,Integer,String,ForeignKey
# 还要从orm 中导入一个 relationship 关系映射
from sqlalchemy.orm import relationship

class ClassTable(Base):
    __tablename__="classtable"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),index=True)

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name = Column(String(32),index=True)

    # 关联字段,让class_id 与 class 的 id 进行关联,主外键关系(这里的ForeignKey一定要是表名.id不是对象名)
    class_id = Column(Integer,ForeignKey("classtable.id"))

    # 将student 与 classtable 创建关系 这个不是字段,只是关系,backref是反向关联的关键字
    to_class = relationship("ClassTable",backref = "stu2class")

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")

Base.metadata.create_all(engine)

