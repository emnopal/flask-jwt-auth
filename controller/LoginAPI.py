from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User
from controller import bcrypt
from helper.encode_auth_token import encode_auth_token


class LoginAPI(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(username=post_data.get('username')).first()
            if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
                auth_token = encode_auth_token(user.username)
                if auth_token:
                    data = {
                        'auth_token': auth_token,
                        'referral_code': user.referral_code
                    }
                    res = response_message(200, 'success', 'Successfully logged in.', data)
                    res.set_cookie('app_session', auth_token, max_age=60 * 60)
                    return res
            else:
                return response_message(404, 'fail', 'User does not exist or username or password not match.')
        except Exception as e:
            return response_message(401, 'fail', f'Username or password not match. {e}')

    def get(self):
        if request.cookies.get('app_session'):
            data = {
                'auth_token': request.cookies.get('app_session')
            }
            return response_message(200, 'success', 'Successfully logged in.', data)
        else:
            return response_message(401, 'fail', 'Session does not exists, Please login.')
