import requests
from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from helper.decode_auth_token import decode_auth_token


class GetHeroName(MethodResource, Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        args = request.args
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
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
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()
