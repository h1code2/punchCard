# -*- encoding: utf-8 -*-
# @Time : 2018/10/26/026 13:00
# @Author : 山那边的瘦子
# @Email : 690238539@qq.com
# @File : manage.py
# @Software: PyCharm

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from exts import db
from models import StudentInfoModel

manage = Manager(app=app)
Migrate(app, db)

manage.add_command('db', MigrateCommand)


@manage.option('-n', '--username', dest='username')
@manage.option('-t', '--telephone', dest='telephone')
@manage.option('-i', '--studentId', dest='studentId')
@manage.option('-p', '--password', dest='password')
def add_stu_info(username, telephone, studentId, password):
    """
    添加成员
    :param username: #姓名
    :param telephone: #手机号
    :param studentId: # 学生ID
    :param password: # 密码
    :return:
    """
    stu = StudentInfoModel(username=username, telephone=telephone, studentId=studentId, password=password)
    db.session.add(stu)
    db.session.commit()
    print('数据添加成功')


@manage.command
def init_stu_info():
    """
    初始化数据完成
    :return:
    """
    stuInfo = [
        {'UserName': '王XX', 'ID': '123456', 'Phone': '18338000000'}
    ]
    for info in stuInfo:
        stu = StudentInfoModel(username=info['UserName'], telephone=info['Phone'], studentId=info['ID'])
        db.session.add(stu)
        db.session.commit()
    print("初始化数据已经完成")


@manage.command
def init_stu_passwd():
    passwd = [
        {
            'UserName': '王XX',
            "Password": '123456789.'
        }
    ]
    for pswd in passwd:
        stu = StudentInfoModel.query.filter_by(username=pswd['UserName']).first()
        if stu:
            stu.password = pswd['Password']
        else:
            print('该人不在原数据库')
        db.session.commit()
    print('密码初始化完成')


if __name__ == '__main__':
    manage.run()
