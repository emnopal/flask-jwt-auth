from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from helper.middleware import middleware
from model import User


class UserAPI(MethodResource, Resource):

    @middleware
    def get(self, auth):
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'referral_code': user.referral_code,
            'registered_on': user.registered_on
        }
        return response_message(200, 'success', 'Successfully get user data.', data)

    @middleware
    def post(self, auth):
        return self.get(auth)
