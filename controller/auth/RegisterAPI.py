from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message, validate_register
from model import User
from controller import db


class RegisterAPI(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
        user = User.query.filter_by(username=post_data.get('username')).first()
        if not user:
            try:
                user = validate_register(post_data)
                db.session.add(user)
                db.session.commit()
                return response_message(201, 'success', 'Successfully registered.')
            except Exception as e:
                return response_message(401, 'fail', str(e))
        else:
            return response_message(202, 'fail', 'User already exists. Please Log in.')
