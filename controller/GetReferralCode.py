from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from middleware import must_login
from model import User


class GetReferralCode(MethodResource, Resource):

    @must_login
    def get(self, auth):
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        data = {
            'referral_code': user.referral_code,
        }
        return response_message(200, 'success', 'Successfully get referral code.', data)

