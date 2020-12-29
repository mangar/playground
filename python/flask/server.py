# -*- coding: utf-8 -*

#
# pip install Flask
#
# export FLASK_ENV=development
# export FLASK_APP=server.py
# flask run
#

from flask import Flask
from flask import request

import base
from controllers.index_controller import IndexController
from base.log import Log

app = Flask(__name__)



flag_debug = base.config['flag_debug']


Log.debug('Flag Debug:' + flag_debug, app)



@app.route('/', methods = ['GET'])
def index():
    Log.debug('Mensagem de DEBUG', app)
    Log.info('Mensagem de INFO', app)
    controller = IndexController(app)
    return controller.index()


@app.route('/hello', methods = ['GET'])
def hello_world():
    return 'Hello, World!'


