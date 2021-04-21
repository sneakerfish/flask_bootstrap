from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, world.</h1><p>Your browser is {}</p>'.format(user_agent)
