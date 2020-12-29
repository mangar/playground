# -*- coding: utf-8 -*

from flask import jsonify


class IndexController:

    def __init__(self, app):
        self.app = app

    #
    #
    def index(self):
        return jsonify(message='Content from IndexController.......')



