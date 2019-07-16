#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 15:37
# @Author  : yuguo
from sqlal.one_more01 import Student, ClassTable,engine

from sqlalchemy.orm import sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 删除
class_info = db_session.query(ClassTable).filter(ClassTable.name=="OldBoyS1").first()
db_session.query(Student).filter(Student.class_id == class_info.id).delete()
db_session.commit()

db_session.close()

