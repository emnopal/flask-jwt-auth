from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User
from helper.decode_auth_token import decode_auth_token


class GetReferralCode(MethodResource, Resource):
    def get(self):
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
                user = User.query.filter_by(username=resp['sub']['username']).first()
                data = {
                    'referral_code': user.referral_code,
                }
                return response_message(200, 'success', 'Successfully get referral code.', data)
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()

