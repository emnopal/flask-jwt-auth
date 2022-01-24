from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User
from controller import db, bcrypt
from helper.decode_auth_token import decode_auth_token


class UpdateUserInformation(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
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
                try:
                    user = User.query.filter_by(username=post_data.get('username')).first()
                    if user and user.username == resp['sub']['username']:
                        if bcrypt.check_password_hash(user.password, post_data.get('password')):
                            try:
                                user.name = post_data.get('name')
                                user.email = post_data.get('email')
                                db.session.commit()
                                return response_message(200, 'success', 'Successfully updated data.')
                            except:
                                return response_message(500, 'fail', 'Email already exists.')
                        else:
                            return response_message(401, 'fail', 'You have no permission to update data.')
                    else:
                        return response_message(404, 'fail', "User doesn't exist.")
                except Exception as e:
                    return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')
        return response_message(401, 'fail', 'Session does not exists or not a valid token, Please login.')

    def put(self):
        return self.post()

    def patch(self):
        return self.post()
