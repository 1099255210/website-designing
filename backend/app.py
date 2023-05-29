from flask import Flask, request, send_file, jsonify
from pymongo import MongoClient
import plun.posterlayout.inference as pl
import plun.posterlayout.u2net.inference as u2
from PIL import Image
from io import BytesIO
from typing import List

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
canvas_width = 513
canvas_height = 750

'''
Routers
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


@app.route('/layout', methods=['POST'])
def get_layout():
  ts = request.json.get('ts')
  # 从文件中读取JSON布局数据并发送回前端
  layout_path = os.path.join(base_path, f'{ts}.json')
  with open(layout_path, 'r') as f:
    layout_data = json.load(f)

  return layout_data


@app.route('/thumbnail', methods=['GET'])
def get_thumbnail():
  # 发送保存的缩略图文件回前端
  thumbnail_path = os.path.join(base_path, 'thumbnail.png')
  send_file(thumbnail_path, mimetype='image/png')
 
 
@app.route('/inference', methods=['POST'])
def get_inference():
  image_data = request.json.get('productImg')
  product_name = request.json.get('productName')
  product_type = request.json.get('productType')
  product_promote = request.json.get('promote')
  
  salnet = app.config['salnet']
  layoutnet = app.config['layoutnet']
  
  image_bytes = base64.b64decode(image_data.split(',')[1])
  image = Image.open(BytesIO(image_bytes))
  result = put_image(image)
  
  image_path = result['image_path']
  position_xywh = result['position']
  
  out_dir = 'data'
  
  ret_path = u2.get_single_saliency(salnet, image_path, out_dir)
  
  print(ret_path)
  
  result = pl.get_single_layout(layoutnet, image_path, ret_path)
  
  cls = result['cls']
  box = result['box']
  
  bb = [{
    'cls': c,
    'box': b,
  } for c, b in zip(cls, box)]
  
  res = arrange_bb(bb, product_name, product_promote)
  
  img_obj = {
    'left': position_xywh[0],
    'top': position_xywh[1],
    'width': position_xywh[2],
    'height': position_xywh[3],
  }
  
  res.append({'obj': 'img', 'option': img_obj})
  
  res_list = [res]
  
  response = {
    'data': {
      'draw_obj': res_list,
    }
  }
  print(response)
  
  return jsonify(response)


'''
Functions
'''

def validate_login(form:dict) -> dict:
  res = collection.find_one({'userName': form['userName']})
  if not res:
    return {'code': -1, 'type': '该用户不存在', 'msg': '请检查用户名输入是否正确或注册新账号'}
  if res['userPwd'] != form['userPwd']:
    return {'code': -1, 'type': '用户名或密码错误', 'msg': '请检查用户名与密码是否正确'}
  return {'code': 0, 'type': '登录成功！', 'msg': '欢迎来到海报设计平台！'}
  

def excute_regist(form:dict) -> dict:
  res = collection.find_one({'userName': form['userName']})
  if res:
    return {'code': -1, 'type': '用户名已被注册', 'msg': '请更换用户名'}
  collection.insert_one(form)
  return {'code': 0, 'type': '注册成功', 'msg': '欢迎您成为我们的一员！'}


def put_image(img: Image.Image, bg="", layout_size=(canvas_width, canvas_height), mode='b') -> dict:
  width, height = img.size
  scale_ratio = min(layout_size[0] / width, layout_size[1] / height)
  new_size = (int(width * scale_ratio), int(height * scale_ratio))

  img = img.resize(new_size)

  if mode == 'b':
    x = int((layout_size[0] - new_size[0]) / 2)
    y = layout_size[1] - new_size[1]
  elif mode == 't':
    x = int((layout_size[0] - new_size[0]) / 2)
    y = 0
  elif mode == 'tl':
    x = 0
    y = 0
  elif mode == 'tr':
    x = layout_size[0] - new_size[0]
    y = 0
  elif mode == 'bl':
    x = 0
    y = layout_size[1] - new_size[1]
  elif mode == 'bl':
    x = layout_size[0] - new_size[0]
    y = layout_size[1] - new_size[1]

  if not bg:
    canvas = Image.new('RGB', (layout_size[0], layout_size[1]), color=(255, 255, 255))
    canvas.paste(img, (x, y))
    image_path = os.path.join(base_path, f'{mode}.png')
    canvas.save(image_path)

  return { 'image_path': image_path, 'position': [x, y, new_size[0], new_size[1]] }

def cover(index, boxes):
  target_box = boxes[index]
  max_overlap = 0
  max_overlap_index = None
  
  for i, box in enumerate(boxes):
    if i == index:
      continue

    bb1 = box['bb']
    bb2 = target_box['bb']

    # 计算两个框的交集面积
    intersection_area = max(0, min(bb1[2], bb2[2]) - max(bb1[0], bb2[0])) * max(0, min(bb1[3], bb2[3]) - max(bb1[1], bb2[1]))
    
    # 计算覆盖率
    overlap = intersection_area / ((bb1[2] - bb1[0]) * (bb1[3] - bb1[1]))
    
    if overlap > max_overlap:
      max_overlap = overlap
      max_overlap_index = i
  
  return max_overlap_index

def arrange_bb(bb:List[dict], product_name:str, product_promote:List[str]):
  
  result_obj = []
  
  # arrange name
  for item in bb:
    if item['cls'] == 2:
      b = item['box']
      left = (b[2] + b[0]) // 2
      top = (b[3] + b[1]) // 2
      name_obj = {
        'left': left,
        'top': top,
        'fontSize': 80,
        'fontFamily': 'SourceHanSans-Bold',
        'text': product_name,
      }
      result_obj.append({'obj': 'name', 'option': name_obj})
      break
 
  # arrange promote
  for p in product_promote:
    for idx, item in enumerate(bb):
      if item['cls'] == 1 and not 'used' in item:
        item['used'] = 1
        b = item['box']
        left = (b[2] + b[0]) // 2
        top = (b[3] + b[1]) // 2
        p_obj = {
          'left': left,
          'top': top,
          'fontSize': 30,
          'fontFamily': 'SourceHanSans-Bold',
          'text': p,
        }
        result_obj.append({'obj': 'promote', 'option': p_obj})
        break
        # iou_max_idx = cover(idx, bb)
        # if bb[iou_max_idx]['cls'] == 3:
      
  return result_obj
  ...  


if __name__ == '__main__':
  app.config['salnet'] = u2.initialize_model()
  app.config['layoutnet'] = pl.initialize_model()
  app.run(port=app.config['PORT'])