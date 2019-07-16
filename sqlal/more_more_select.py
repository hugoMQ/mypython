#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 15:50
# @Author  : yuguo
from sqlal.more_more01 import Girl,Boy,Hotel,engine

# 创建连接
from sqlalchemy.orm import sessionmaker
# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.通过Boy查询约会过的所有Girl
hotel = db_session.query(Boy).all()
for row in hotel:
    for row2 in row.girl2boy:
        print(row.name,row2.name)

# 2.通过Girl查询约会过的所有Boy
hotel = db_session.query(Girl).all()
for row in hotel:
    for row2 in row.boys:
        print(row.name,row2.name)
