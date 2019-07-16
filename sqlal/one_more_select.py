#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 15:31
# @Author  : yuguo
from sqlal.one_more01 import Student, ClassTable,engine

from sqlalchemy.orm import sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.查询所有数据,并显示班级名称,连表查询
student_list = db_session.query(Student).all()
for row in student_list:
    # row.to_class.name 通过Student对象中的关系字段relationship to_class 获取关联 ClassTable中的name
    print(row.name,row.to_class.name,row.class_id)

# 2.反向查询
class_list = db_session.query(ClassTable).all()
for row in class_list:
    for row2 in row.stu2class:
        print(row.name,row2.name)
# row.stu2class 通过 backref 中的 stu2class 反向关联到 Student 表中根据ID获取name


db_session.close()

