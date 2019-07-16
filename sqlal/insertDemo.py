#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 10:31
# @Author  : yuguo

#insert 为数据表增加数据
# insert One 增加一行数据
# insert into user(name) values ("谢霆锋")
# 在ORM中的操作:
# 1.首先导入之间做好的ORM 对象 User
from sqlal.my_create_table import User
# 2.使用Users ORM模型创建一条数据
user1 = User(name="谢霆锋")
# 数据已经创建完了,但是需要写入到数据库中啊,怎么写入呢?
# 3.写入数据库:
# 首先打开数据库会话 , 说白了就是创建了一个操纵数据库的窗口
# 导入 sqlalchemy.orm 中的 sessionmaker
from sqlalchemy.orm import sessionmaker
# 导入之前创建好的 create_engine
from sqlal.my_create_table import engine
# 创建 sessionmaker 会话对象,将数据库引擎 engine 交给 sessionmaker
Session = sessionmaker(engine)
# 打开会话对象 Session
db_session = Session()
# 在db_session会话中添加一条 UserORM模型创建的数据
db_session.add(user1)
# 使用 db_session 会话提交 , 这里的提交是指将db_session中的所有指令一次性提交
db_session.commit()

# 当然也你也可很任性的提交多条数据
# 方法一:
user2 = User(name="赵丽颖")
user3 = User(name="冯绍峰")
db_session.add(user2)
db_session.add(user3)
db_session.commit()
# 之前说过commit是将db_session中的所有指令一次性提交,现在的db_session中至少有两条指令user2和user3
db_session.close()
#关闭会话

# 如果说你觉得方法一很麻烦,那么方法二一定非常非常适合你
# 方法二:
user_list = [
    User(name="葫芦娃1"),
    User(name="葫芦娃2"),
    User(name="葫芦娃3")
]
db_session.add_all(user_list)
db_session.commit()

db_session.close()

