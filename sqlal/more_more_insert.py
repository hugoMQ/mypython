#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 15:46
# @Author  : yuguo
from sqlal.more_more01 import Girl,Boy,Hotel,engine

# 创建连接
from sqlalchemy.orm import sessionmaker
# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.通过Boy添加Girl和Hotel数据
# boy = Boy(name="DragonFire")
# boy.girl2boy = [Girl(name="赵丽颖"),Girl(name="Angelababy")]
# db_session.add(boy)
# db_session.commit()

# 2.通过Girl添加Boy和Hotel数据
girl = Girl(name="珊珊")
girl.boys = [Boy(name="Dragon")]
db_session.add(girl)
db_session.commit()

