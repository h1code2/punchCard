import json
import random
import time

import requests
from flask import Flask, jsonify, request,render_template

from config import Config as config
from exts import db
from models import StudentInfoModel

requests.packages.urllib3.disable_warnings()

req = requests.session()

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/punchCard/', methods=['POST'])
def punchCard():
    """
    自动签到
    :return: json
    """
    code = request.form.get('code')
    stus = StudentInfoModel.query.filter_by().all()
    result = []
    for index, stu in enumerate(stus):
        UserAgent = random.choice(config.headers)
        if stu.password is not None:
            # 登录
            login = req.post(url=config.URL_PATH + '/AppCode/LoginInfo.ashx', data={
                'action': 'loginmb',
                'loginname': stu.telephone,
                'password': stu.password
            }, headers=UserAgent, verify=False)
            print(login.cookies['ASP.NET_SessionId'])
            time.sleep(random.randint(1, 2))
            # 签到
            pCard = req.post(
                url=config.URL_PATH + '/_CheckIn/CheckIn.ashx',
                data={
                    'action': 'studentcheckin',
                    'studentid': stu.studentId,
                    'checkincode': code
                },
                headers=UserAgent,
                verify=False)
            print(pCard.text)
            jsonObj = json.loads(pCard.text)
            data = {}
            data['name'] = stu.username
            data['msg'] = jsonObj['msgbox'][:6]
            result.insert(index, data)
            req.cookies.clear()

    # for
    return jsonify({
        'code': '0',
        'message': '任务完成',
        'data': result
    })


def handle():
    pass


if __name__ == '__main__':
    app.run()
