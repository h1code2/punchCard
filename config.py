# -*- encoding: utf-8 -*-
# @Time : 2018/10/26/026 12:55
# @Author : 山那边的瘦子
# @Email : 690238539@qq.com
# @File : config.py
# @Software: PyCharm

class Config(object):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = ''
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'punchCard'

    # mysql数据库连接信息,这里改为自己的账号
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                           DRIVER,
                                                                           USERNAME,
                                                                           PASSWORD,
                                                                           HOST,
                                                                           PORT,
                                                                           DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True

    URL_PATH = 'https://www.duifene.com'

    headers = [
        {
            'User-Agent': 'mozilla/5.0 (linux; android 5.1.1; mi note pro build/lmy47v) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/37.0.0.0 mobile mqqbrowser/6.2 tbs/036215 safari/537.36 micromessenger/6.3.16.49_r03ae324.780 nettype/wifi language/zh_cn'
        }, {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; Lenovo A808t Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.1.550 U3/0.8.0 Mobile Safari/534.30'
        }, {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI'
        }
    ]
