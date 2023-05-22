from flask import Flask, request, send_file, jsonify
from pymongo import MongoClient

import json
import os
import base64

import mainneon

'''
Please run this in port 2145
'''

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['PORT'] = 2145

mongouri = 'mongodb://localhost:27017'
base_path = './data'
client = MongoClient(mongouri)
db = client['test']
collection = db['users']

'''
Routes
'''

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

@app.route('/exportToTimeline', methods=['POST'])
def exportToTimeline():
  # 获取POST请求中的参数
  timestamp = request.json.get('ts')
  imageData = request.json.get('img')
  jsonData = request.json.get('json')
  
  imgPath = os.path.join(base_path, f"{timestamp}.png")
  jsonPath = os.path.join(base_path, f"{timestamp}.json")

  with open(imgPath, "wb") as f:
    f.write(base64.b64decode(imageData.split(',')[1]))

  with open(jsonPath, "w") as f:
    json.dump(jsonData, f)

  response = {'status': 'success'}
  return jsonify(response)

@app.route('/export', methods=['POST'])
def export_canvas():
  data = request.json

  image_data = data['image']
  json_data = data['json']

  img_data = base64.b64decode(image_data.split(',')[1])
  image_path = os.path.join(base_path, 'canvas.png')
  with open(image_path, 'wb') as f:
    f.write(img_data)

  layout_path = os.path.join(base_path, 'layout.json')
  with open(layout_path, 'w') as f:
    f.write(json.dumps(json_data))

  return 'Export successful'


@app.route('/layout', methods=['GET'])
def get_layout():
  # 从文件中读取JSON布局数据并发送回前端
  layout_path = os.path.join(base_path, 'layout.json')
  with open(layout_path, 'r') as f:
    layout_data = json.load(f)

  return layout_data


@app.route('/thumbnail', methods=['GET'])
def get_thumbnail():
  # 发送保存的缩略图文件回前端
  thumbnail_path = os.path.join(base_path, 'thumbnail.png')
  send_file(thumbnail_path, mimetype='image/png')


'''
Functions
'''

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


if __name__ == '__main__':
  app.run(port=app.config['PORT'])