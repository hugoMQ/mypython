#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 10:52
# @Author  : yuguo
# ORM 删除一条多条数据
# 老规矩
# 导入 ORM 创建会话
from sqlal.my_create_table import User,engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# DELETE FROM `user` WHERE id=20
res = db_session.query(User).filter(User.id==3).delete()
print(res)
# 是删除操作吧,没错吧,那你想什么呢?commit吧
db_session.commit()

db_session.close()
#关闭会话

