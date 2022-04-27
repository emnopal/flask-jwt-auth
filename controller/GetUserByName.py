from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from model import User
from middleware import must_login


class GetUserByName(MethodResource, Resource):

    @must_login
    def get(self, auth):

        args = request.args
        data = {}

        # Get user based by name or mail or username
        if args:

            by_name = args.get('name')
            by_username = args.get('username')
            by_mail = args.get('mail')

            if by_name:
                result = User.query.filter(User.name.contains(by_name)).all()
            if by_username:
                result = User.query.filter(User.username.contains(by_username)).all()
            if by_mail:
                result = User.query.filter(User.email.contains(by_mail)).all()

            for num, user in enumerate(result):
                data[f'user_{num}'] = {
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'referral_code': user.referral_code,
                    'registered_on': user.registered_on
                }
            return response_message(200, 'success', 'Successfully get user data.', data)

        # Return all user
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

