from flask import request
from helper import response_message, decode_auth_token

from src import app


def must_login(func):
    def wrapper(self, *args, **kwargs):
        conf = app.config
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get(conf.get('COOKIE_NAME'))
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed. Please provide a valid token or login or register to continue.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                auth_data = {
                    'auth_token': auth_token,
                    'auth_header': auth_header,
                    'auth_cookie': auth_cookie,
                    'resp': resp,
                }
                return func(self, auth_data)
            else:
                return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Token not valid, please login or register to continue.')
    return wrapper
