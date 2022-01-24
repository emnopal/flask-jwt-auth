from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User, BlacklistToken
from controller import db
from helper.decode_auth_token import decode_auth_token


class LogoutAPI(MethodResource, Resource):
    def post(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
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
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    db.session.add(blacklist_token)
                    db.session.commit()
                    res = response_message(200, 'success', 'Successfully logged out.')
                    res.set_cookie('app_session', '', expires=0)
                    return res
                except Exception as e:
                    return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')
            else:
                return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def get(self):
        return self.post()

    def delete(self):
        return self.post()
