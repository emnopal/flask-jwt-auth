from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User
from middleware.must_login import must_login


class FindByName(MethodResource, Resource):

    @must_login
    def get(self, auth):
        args = request.args
        data = {}
        if args:
            users = User.query.filter(User.name.contains(args.get('name'))).all()
            for num, user in enumerate(users):
                data[f'user_{num}'] = {
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'referral_code': user.referral_code,
                    'registered_on': user.registered_on
                }
            return response_message(200, 'success', 'Successfully get user data.', data)
        users = User.query.all()
        for num, user in enumerate(users):
            data[f'user_{num}'] = {
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'referral_code': user.referral_code,
                'registered_on': user.registered_on
            }
        return response_message(200, 'success', 'Successfully get user data.', data)

    @must_login
    def post(self, auth):
        return self.get(auth)
