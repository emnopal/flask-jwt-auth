from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from model import User
from middleware import must_login


class GetCurrentUser(MethodResource, Resource):

    @must_login
    def get(self, auth):
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'referral_code': user.referral_code,
            'registered_on': user.registered_on,
            'auth_token': auth
        }
        return response_message(200, 'success', 'Successfully get session data.', data)

