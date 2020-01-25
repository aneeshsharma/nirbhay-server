from app import app
from flask import request


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
