from flask import Flask
from flask import request
from pymongo import MongoClient

import mainneon

'''
Please run this in port 2145
'''

app = Flask(__name__)

mongouri = 'mongodb://localhost:27017'
client = MongoClient(mongouri)
db = client['test']
collection = db['users']

@app.route('/login', methods=['POST'])
def login():
  res = request.json
  userName = res['userName']
  userPwd = res['userPwd']
  return validate_login({'userName': userName, 'userPwd': userPwd})


@app.route('/regist', methods=['POST'])
def regist():
  res = request.json
  userName = res['userName']
  userPwd = res['userPwd']
  return excute_regist({'userName': userName, 'userPwd': userPwd})


@app.route('/gifgen', methods=['POST'])
def gifgen():
  res = request.json
  words = res['words'].split('\n')
  direction = res['direction']
  duration = 5
  if ("time" in res):
    duration = res['time']
  print(words, direction, duration)
  imgpath = mainneon.generate(words, duration, direction)
  print(imgpath)
  return imgpath


@app.route('/save', methods=['POST'])
def save():
  res = request.json
  print(res)


def validate_login(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if not res:
    return {'code': -1, 'type': '该用户不存在', 'msg': '请检查用户名输入是否正确或注册新账号'}
  if res['userPwd'] != form['userPwd']:
    return {'code': -1, 'type': '用户名或密码错误', 'msg': '请检查用户名与密码是否正确'}
  return {'code': 0, 'type': '登录成功！', 'msg': '欢迎来到海报设计平台！'}
  

def excute_regist(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if res:
    return {'code': -1, 'type': '用户名已被注册', 'msg': '请更换用户名'}
  collection.insert_one(form)
  return {'code': 0, 'type': '注册成功', 'msg': '欢迎您成为我们的一员！'}