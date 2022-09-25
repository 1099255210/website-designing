const { request } = require('express');
const express = require('express')
const app = express()
const mongoose = require('mongoose');

var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false })

const uri = 'mongodb://localhost:27017/test'
const User = mongoose.model('user', {
  userName: String,
  userPwd: String
});

mongoose.connect(uri);

mongoose.connection.on('open', () => {
  // 网站响应

  // 登录
  app.post('/login', urlencodedParser, (req, res) => {
    var request = {
      'userName':req.body.userName,
      'userPwd':req.body.userPwd
    };
    User.find({'userName': request.userName}, (err, doc) => {
      if (err) throw err;
      if (doc.length) {
        if (request.userPwd === doc[0].userPwd) {
          res.send('用户登录成功');
        }
        else {
          res.send('密码错误');
        }
      }
      else res.send('无该用户名，请注册');
    })
  })

  app.post('/register', urlencodedParser, (req, res) => {
    var request = {
      'userName':req.body.userName,
      'userPwd':req.body.userPwd
    };
    User.find({'userName': request.userName}, (err, doc) => {
      if (err) throw err;

      console.log(doc);
      if (doc.length) {
        res.send('已经注册');
      }
      else {
        const user = new User(request);
        user.save().then(() => res.send('用户注册成功'));
      }
    })
  })

  app.listen(2145, () => {
    console.log('服务启动');
  })

})