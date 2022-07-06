from flask import request
from helper import response_message, Auth
from model import BlacklistToken


def TokenRequired(func):
    def wrapper(self, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                if BlacklistToken.query.filter_by(token=auth_header).first():
                    raise ValueError()
                auth_token = auth_header.split(" ")[1]
            except Exception:
                return response_message(401, 'fail', 'Token is Invalid')
        else:
            auth_token = ''
        if auth_token:
            resp = Auth(token=auth_token).DecodeAuthToken()
            if not isinstance(resp, str):
                auth_data = {
                    'auth_token': auth_token,
                    'auth_header': auth_header,
                    'resp': resp,
                }
                return func(self, auth_data, **kwargs)
            else:
                return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Token not valid, please login or register to continue.')
    return wrapper
