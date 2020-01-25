from app import app
from flask import request
from app import register_data as rd


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/login', methods=["POST", "GET"])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            return username + " | " + password
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
            return str(user_data)

        return "Invalid Request"
    except Exception as e:
        return "Exception : " + str(e)
