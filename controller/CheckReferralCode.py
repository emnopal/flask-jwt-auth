from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from middleware import must_login
from model import User


class CheckReferralCode(MethodResource, Resource):

    @must_login
    def post(self, auth):
        """
        Using json to send referral code
        """
        post_data = request.get_json()
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        if user.referral_code != post_data['referral_code']:
            if User.query.filter_by(referral_code=post_data['referral_code']).first():
                return response_message(200, 'success', 'Valid referral code.')
        return response_message(401, 'fail', 'Invalid referral code.')

    @must_login
    def get(self, auth):
        """
        Using query parameter to send referral code
        """
        args = request.args
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        if user.referral_code != args.get('ref'):
            if User.query.filter_by(referral_code=args.get('ref')).first():
                return response_message(200, 'success', 'Valid referral code.')
        return response_message(401, 'fail', 'Invalid referral code.')
