from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message, check_mail
from model import User
from controller import db


class RegisterAPI(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
        user = User.query.filter_by(username=post_data.get('username')).first()
        if not user:
            try:
                user = User(
                    username=str(post_data.get('username')),
                    password=str(post_data.get('password')),
                    email=check_mail(post_data.get('email')),
                    name=str(post_data.get('name'))
                )
                db.session.add(user)
                db.session.commit()
                return response_message(201, 'success', 'Successfully registered.')
            except Exception:
                return response_message(401, 'fail', 'Some error occurred. Please try again.')
        else:
            return response_message(202, 'fail', 'User already exists. Please Log in.')
