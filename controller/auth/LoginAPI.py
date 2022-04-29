from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from model import User
from controller import bcrypt, app
from helper import encode_auth_token


class LoginAPI(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
        conf = app.config
        try:
            user = User.query.filter_by(username=post_data.get('username')).first()
            if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
                auth_token = encode_auth_token(user.username, int(conf.get('TOKEN_EXPIRED')))
                if auth_token:
                    data = {
                        'auth_token': auth_token,
                        'referral_code': user.referral_code
                    }
                    res = response_message(200, 'success', 'Successfully logged in.', data)
                    res.set_cookie(conf.get('COOKIE_NAME'), auth_token, max_age=60 * conf.get('TOKEN_EXPIRED'))
                    return res
            else:
                return response_message(404, 'fail', 'User does not exist or username or password not match.')
        except Exception as e:
            return response_message(401, 'fail', f'Username or password not match. {e}')
