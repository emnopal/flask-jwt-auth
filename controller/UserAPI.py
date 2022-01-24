from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from middleware.must_login import must_login
from model import User


class UserAPI(MethodResource, Resource):

    @must_login
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

    @must_login
    def post(self, auth):
        return self.get(auth)
