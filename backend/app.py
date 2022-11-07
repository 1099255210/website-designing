from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

mongouri = 'mongodb://localhost:27017'
client = MongoClient(mongouri)
db = client['test']
collection = db['users']

@app.route('/login', methods=['POST'])
def login():
  userName = request.form['userName']
  userPwd = request.form['userPwd']
  return validate_login({'userName': userName, 'userPwd': userPwd})

@app.route('/regist', methods=['POST'])
def regist():
  userName = request.form['userName']
  userPwd = request.form['userPwd']
  return excute_regist({'userName': userName, 'userPwd': userPwd})


def validate_login(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if not res:
    return 'User does not exists.'
  if res['userPwd'] != form['userPwd']:
    return 'Password wrong.'
  return 'Login successful.'


def excute_regist(form:dict):
  res = collection.find_one({'userName': form['userName']})
  if res:
    return 'User has been registered.'
  collection.insert_one(form)
  return 'Register successful.'