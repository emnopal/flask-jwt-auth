import requests
from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from middleware.must_login import must_login


class GetHeroName(MethodResource, Resource):

    @must_login
    def get(self, auth):
        args = request.args
        data = {}
        r = requests.get('https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
        if args:
            for key, value in r.json()['data'].items():
                if args.get('q').title() in key:
                    data[key] = value
                    return response_message(200, 'success', 'Successfully get hero data.', data)
        for key, value in r.json()['data'].items():
            data[key] = value
            return response_message(200, 'success', 'Successfully get hero data.', data)

    @must_login
    def post(self, auth):
        return self.get(auth)
