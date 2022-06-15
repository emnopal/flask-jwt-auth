import datetime
from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message, encode_auth_token
from model import User
from controller import bcrypt, app, db


class LoginAPI(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
        conf = app.config
        try:
            user = User.query.filter_by(username=str(post_data.get('username'))).first()
            if user and bcrypt.check_password_hash(str(user.password), str(post_data.get('password'))):
                auth_token = encode_auth_token(str(user.username), int(conf.get('TOKEN_EXPIRED')))
                if auth_token:
                    user.last_logged_in = datetime.datetime.now()
                    user.last_logged_out = None
                    db.session.commit()
                    data = {
                        'auth_token': auth_token,
                        'referral_code': user.referral_code
                    }
                    return response_message(200, 'success', 'Successfully logged in.', data)
            else:
                return response_message(404, 'fail', 'User does not exist or username or password not match.')
        except Exception as e:
            return response_message(401, 'fail', f'Username or password not match. {e}')
