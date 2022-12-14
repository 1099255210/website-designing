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
  # userName = request.form['userName']
  # userPwd = request.form['userPwd']
  # return validate_login({'userName': userName, 'userPwd': userPwd})

@app.route('/regist', methods=['POST'])
def regist():
  res = request.json
  userName = res['userName']
  userPwd = res['userPwd']
  return excute_regist({'userName': userName, 'userPwd': userPwd})
  # userName = request.form['userName']
  # userPwd = request.form['userPwd']
  # return excute_regist({'userName': userName, 'userPwd': userPwd})

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


def validate_login(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if not res:
    return {'code': -1, 'msg': 'User does not exists.'}
  if res['userPwd'] != form['userPwd']:
    return {'code': -1, 'msg': 'Password wrong.'}
  return {'code': 0, 'msg': 'Login successful.'}
  

def excute_regist(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if res:
    return {'code': -1, 'msg': 'User has been registered.'}
  collection.insert_one(form)
  return {'code': -1, 'msg': 'Register successful.'}