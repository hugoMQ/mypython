#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-16 14:29
# @Author  : yuguo
from sqlal.one_more01 import Student, ClassTable,engine
# 创建连接
from sqlalchemy.orm import sessionmaker
# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 增加数据
# 1.简单增加数据
# 添加两个班级:
# db_session.add_all([
#     ClassTable(name="OldBoyS1"),
#     ClassTable(name="OldBoyS2")
# ])
# db_session.commit()
# 添加一个学生 DragonFire 班级是 OldBoyS1
# 查询要添加到的班级
# class_obj = db_session.query(ClassTable).filter(ClassTable.name == "OldBoyS1").first()
# # 创建学生
# stu = Student(name="DragonFire",class_id = class_obj.id)
# db_session.add(stu)
# db_session.commit()

# 2. relationship版 添加数据
# 通过关系列 to_class 可以做到两件事
# 第一件事 在ClassTable表中添加一条数据
# 第二件事 在Student表中添加一条数据并将刚刚添加的ClassTable的数据id填写在Student的class_id中
# stu_cla = Student(name="DragonFire",to_class=ClassTable(name="OldBoyS3"))
# print(stu_cla.name,stu_cla.class_id)
# db_session.add(stu_cla)
# db_session.commit()

# 3.relationship版 反向添加数据
# 首先建立ClassTable数据
class_obj = ClassTable(name="OldBoyS2")
# 通过class_obj中的反向关联字段backref - stu2class
# 向 Student 数据表中添加 2条数据 并将 2条数据的class_id 写成 class_obj的id
class_obj.stu2class = [Student(name="BMW"),Student(name="Audi")]
db_session.add(class_obj)
db_session.commit()

# 关闭连接
db_session.close()

