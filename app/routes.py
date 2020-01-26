from app import app
from flask import request
from app import register_data as rd


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
            return "Content-Type: application/json {\"key\" : \"" + key + "\"}"
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
