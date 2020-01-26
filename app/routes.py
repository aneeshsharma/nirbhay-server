from app import gender_check as gc
from app import app
from flask import request
from flask import Response
from app import register_data as rd
from app import gender_check as gc
import base64
import string
import random


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/login', methods=["POST"])
def login():
    try:
        if request.method == 'POST':
            print(request.form['username'] + " | " + request.form['password'])
            username = request.form['username']
            password = request.form['password']
            key = rd.get_key(username, password)
            resp = Response(key)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Content-Type'] = 'text'
            return resp
        print('Invalid')
        return "Invalid Request"
    except Exception as e:
        return "Exception : " + str(e)


@app.route('/register', methods=['POST'])
def register():
    user_data = {}
    try:
        if request.method == 'POST':
            user_data = request.form
            if not rd.verify(user_data):
                return "FAILED:NO_DATA"
            return rd.register(user_data)

        return "Invalid Request"
    except Exception as e:
        return "Exception : " + str(e)


@app.route('/mirror', methods=['POST'])
def mirror():
    return str(request.form)


@app.route('/update_location', methods=['POST'])
def location():
    try:
        if request.method == 'POST':
            lat = request.form['lat']
            lng = request.form['lng']
            key = request.form['key']
            return rd.update_location(lat, lng, key)
    except Exception as e:
        return str(e)


@app.route('/update_dest', methods=['POST'])
def destination():
    try:
        if request.method == 'POST':
            lat = request.form['destLat']
            lng = request.form['destLng']
            key = request.form['key']
            return rd.update_dest(lat, lng, key)
    except Exception as e:
        return str(e)


@app.route('/travel', methods=['POST'])
def travel():
    try:
        lat = request.form['lat']
        lng = request.form['lng']
        destLat = request.form['destLat']
        destLng = request.form['destLng']
        key = request.form['secret_key']
        return rd.travel_reg(lat, lng, destLat, destLng, key)
    except Exception as e:
        return str(e)


@app.route('/gender', methods=['POST'])
def gender():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_data = request.form['image']
    fileName = ''.join([random.choice(
        string.ascii_lowercase + string.digits) for _ in range(20)]) + ".jpg"
    fileName = dir_path+'/image_chache/' + fileName
    data = base64.decodebytes(image_data.encode('utf-8'))
    with open(fileName, "wb") as f:
        f.write(data)
        f.close()
    resp = Response(gc.findGender(fileName, dir_path))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
