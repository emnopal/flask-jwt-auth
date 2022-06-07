from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from middleware import must_login
from model import User
from controller import db, bcrypt


class UpdateUserInformation(MethodResource, Resource):

    @must_login
    def patch(self, auth):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(username=str(post_data.get('username'))).first()
            if user and user.username == auth['resp']['sub']['username']:
                if bcrypt.check_password_hash(user.password, str(post_data.get('password'))):
                    try:
                        user.name = str(post_data.get('name'))
                        user.email = str(post_data.get('email'))
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

