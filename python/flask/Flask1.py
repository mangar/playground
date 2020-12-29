# -*- coding: utf-8 -*

#
# pip install Flask
#
# export FLASK_ENV=development
# export FLASK_APP=Flask1.py
# flask run
#

from flask import Flask
from flask import request


app = Flask(__name__)



@app.route('/', methods = ['GET'])
def index():
    return 'index'


@app.route('/hello', methods = ['GET'])
def hello_world():
    return 'Hello, World!'