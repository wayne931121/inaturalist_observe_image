import cv2
import requests
import urllib.parse
import json
import numpy as np
from flask import Flask
from flask import request, Response, jsonify
from flask import render_template

def process_image(img): #file_name, file path and name, example: C://Folder1/123.jpg
    img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    size = img.shape
    width, height = 0,0
    if size[0]>size[1]: #size[0] to 1024
        width = 1024
        height = int(size[1]*(width/size[0]))
    else: #size[1] to 1024
        height = 1024
        width = int(size[0]*(height/size[1]))
    image = cv2.resize(img, (width,height))
    image = cv2.imencode(".jpg", image)[1].tobytes()
    return image

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
          "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjo3MDA4MzM5LCJleHAiOjE2ODYzNzQ5ODZ9.X9Nk-9IKhUoVZlpgt75OVYZnvCXjcSD62kZvWsUet5zOOzk4xRjgZ0xlM4RzNRLdnz0mBDfRg8pLr4js2O1EKQ",
           "Origin": "https://www.inaturalist.org",
           "Referer": "https://www.inaturalist.org/",
           "X-Via": "inaturalistjs"
}

def observe(img, image_name):
    session = requests.Session()
    image = process_image(img)
    files={"image":(image_name, image)}
    payload = {"observed_on": "2021/11/14 16:11"}
    req = session.post('https://api.inaturalist.org/v1/computervision/score_image', data=payload, headers=headers, files=files)
    result = req.content.decode(encoding="utf-8")
    result = json.loads(result)
    #print(result)
    spcies = []
    for i in result['results']: 
        try:
            spcies.append(i['taxon']['preferred_common_name'])
        except Exception as e:
            spcies.append(i['taxon']['name'])
        #print(spcies[-1])
    try:
        data = {"準確率":"%.2f"%result["common_ancestor"]["score"], "物種分類":result['common_ancestor']['taxon']["preferred_common_name"],"可能物種":spcies}
    except:
        data = {"準確率":"--", "物種分類":"無法辨識至屬，請嘗試裁減圖片，或者重新為生物照張相片","可能物種":spcies}
    datas = json.dumps(data)
    return datas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('c.html')
@app.route('/observe', methods = ["POST"])
def user():
    global data
    name = request.files['imagefile'].filename
    image = request.files['imagefile'].stream.read()
    result = observe(image, name)
    return result,200,{'Access-Control-Allow-Origin':'*','Access-Control-Allow-Headers':'*','Access-Control-Allow-Methods':'POST'}

app.run(debug=1)