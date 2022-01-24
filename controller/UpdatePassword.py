from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from middleware.must_login import must_login
from model import User
from controller import db, bcrypt, app


class UpdatePassword(MethodResource, Resource):

    @must_login
    def post(self, auth):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(username=post_data.get('username')).first()
            if user and user.username == auth['resp']['sub']['username']:
                if bcrypt.check_password_hash(user.password, post_data.get('old_password')):
                    try:
                        user.password = bcrypt.generate_password_hash(
                            post_data.get('new_password'), app.config.get('BCRYPT_LOG_ROUNDS')
                        ).decode('utf-8')
                        db.session.commit()
                        return response_message(200, 'success', 'Successfully changed password.')
                    except:
                        return response_message(500, 'fail', 'Failed changed password.')
                else:
                    return response_message(401, 'fail', 'You have no permission to update data.')
            else:
                return response_message(404, 'fail', "User doesn't exist.")
        except Exception as e:
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')

    @must_login
    def put(self, auth):
        return self.post(auth)

    @must_login
    def patch(self, auth):
        return self.post(auth)
