#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 15:38
# @Author  : yuguo
from sqlalchemy.ext.declarative import declarative_base
#ORM模型
Base = declarative_base()

from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Hotel(Base):
    __tablename__="hotel"
    id=Column(Integer,primary_key=True)
    girl_id = Column(Integer,ForeignKey("girl.id"))
    boy_id = Column(Integer,ForeignKey("boy.id"))

class Girl(Base):
    __tablename__="girl"
    id=Column(Integer,primary_key=True)
    name = Column(String(32),index=True)

    #创建关系  secondary作用？
    boys = relationship("Boy",secondary="hotel",backref="girl2boy")


class Boy(Base):
    __tablename__="boy"
    id=Column(Integer,primary_key=True)
    name = Column(String(32),index=True)


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")

Base.metadata.create_all(engine)

