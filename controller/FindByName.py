from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User
from helper.decode_auth_token import decode_auth_token


class FindByName(MethodResource, Resource):
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
                if args:
                    users = User.query.filter(User.name.contains(args.get('name'))).all()
                    for num, user in enumerate(users):
                        data[f'user_{num}'] = {
                            'username': user.username,
                            'name': user.name,
                            'email': user.email,
                            'referral_code': user.referral_code,
                            'registered_on': user.registered_on
                        }
                    return response_message(200, 'success', 'Successfully get user data.', data)
                users = User.query.all()
                for num, user in enumerate(users):
                    data[f'user_{num}'] = {
                        'username': user.username,
                        'name': user.name,
                        'email': user.email,
                        'referral_code': user.referral_code,
                        'registered_on': user.registered_on
                    }
                return response_message(200, 'success', 'Successfully get user data.', data)
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()
