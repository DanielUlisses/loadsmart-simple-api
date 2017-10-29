# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class ElbElbname(Resource):

    def get(self, elbName):

        return [], 200, None

    def post(self, elbName):
        print(g.json)

        return {'instanceId': 'something', 'instanceType': 'something', 'launchDate': 'something'}, 201, None

    def delete(self, elbName):
        print(g.json)

        return {'instanceId': 'something', 'instanceType': 'something', 'launchDate': 'something'}, 201, None