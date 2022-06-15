from flask import request
from helper import response_message, decode_auth_token
from model import BlacklistToken
from src import app


def must_login(func):
    def wrapper(self, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                blacklist_token = BlacklistToken.query.filter_by(token=auth_header).first()
                if blacklist_token: raise ValueError()
                auth_token = auth_header.split(" ")[1]
            except Exception as e:
                return response_message(401, 'fail', 'Bearer token malformed. Please provide a valid token or login or register to continue.')
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                auth_data = {
                    'auth_token': auth_token,
                    'auth_header': auth_header,
                    'resp': resp,
                }
                return func(self, auth_data)
            else:
                return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Token not valid, please login or register to continue.')
    return wrapper
