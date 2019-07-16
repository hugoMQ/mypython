#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 10:37
# @Author  : yuguo
# ORM操作查询数据
# 有了刚才Insert增加数据的经验,那么查询之前的准备工作,就不用再重复了吧
# 回想一下刚才Insert时我们的操作
from sqlal.my_create_table import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()

# 1. select * from user 查询user表中的所有数据
# 语法是这样的 使用 db_session 会话 执行User表 query(User) 取出全部数据 all()
user_all_list = db_session.query(User).all()
print(user_all_list)  # [<my_create_table.User object at 0x0000016D7C4BCDD8>]
# 如何查看user_all_list其中的数据呢? 循环呗
for i in user_all_list:
    print(i.id, i.name)  # ORM对象 直接使用调用属性的方法 拿出对应字段的值

db_session.close()
#关闭会话

# 2. select * from user where id >= 20
# 语法是这样的 使用 db_session 会话 执行User表 query(User) 筛选内容User.id >=20 的数据全部取出 all()
user_all_list = db_session.query(User).filter(User.id >= 2).all()
print(user_all_list)
for i in user_all_list:
    print(i.id, i.name)

db_session.close()
#关闭会话

# 3. 除了取出全部还可以只取出一条
user = db_session.query(User).filter(User.id >= 2).first()
print(user.id,user.name)
db_session.close()
#关闭会话

# 4. 乌龙 之 忘了取出数据.......
wulong1 = db_session.query(User).filter(User.id >= 20)
print(wulong1)
#SELECT user.id AS user_id, user.name AS user_name
#FROM user
#WHERE user.id >= %(id_1)s
# Fuck我忘了取出数据了!!!!!!! 哎? wulong1给我显示了原生SQL语句,因祸得福了
wulong2 = db_session.query(User)
print(wulong2)
print(wulong2.first().id)
#SELECT user.id AS user_id, user.name AS user_name
#FROM user
# Fuck我又忘了取出数据了!!!!!!! 哎? wulong2给我显示了原生SQL语句,因祸得福了
db_session.close()
#关闭会话
