from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from helper.decode_auth_token import decode_auth_token


class CurrentSession(MethodResource, Resource):
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
                if args.get('decode') in ['true', 'True', 1, '1']:
                    data = {
                        'auth_token': request.cookies.get('app_session'),
                        'decoded_token': resp
                    }
                    return response_message(200, 'success', 'Successfully get session data.', data)
                data = {
                    'auth_token': request.cookies.get('app_session'),
                }
                return response_message(200, 'success', 'Successfully get session data.', data)
        return response_message(401, 'fail', 'Session does not exists or not a valid token, Please login.')

    def post(self):
        return self.get()