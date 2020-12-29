# -*- coding: utf-8 -*

from flask import jsonify


class HelpController:

    def __init__(self, app):
        self.app = app

    #
    #
    def index(self):
        return jsonify(methods= ['/', '/help', '/hello'])

