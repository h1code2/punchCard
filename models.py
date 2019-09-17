# -*- encoding: utf-8 -*-
# @Time : 2018/10/26/026 13:05
# @Author : 山那边的瘦子
# @Email : 690238539@qq.com
# @File : models.py
# @Software: PyCharm

from exts import db


class StudentInfoModel(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(5), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=True)
    telephone = db.Column(db.String(11), nullable=False, unique=True)
    studentId = db.Column(db.String(10), nullable=False, unique=True)
