#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 9:56
# @Author  : yuguo

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s'%self.name