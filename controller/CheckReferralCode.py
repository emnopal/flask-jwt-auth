from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from helper import response_message, RequestResponse, RequestPost
from middleware import TokenRequired
from model import User


class CheckReferralCodeRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    referral_code = fields_.Str(required=True, description="Input Field for Referral Code, this is required")


class CheckReferralCode(MethodResource):
    fields = CheckReferralCodeRequestPost.fields_

    @doc(
        description='Check Referral Code',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(CheckReferralCodeRequestPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        """
        Using json to send referral code
        """
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        if user.referral_code != kwargs['referral_code']:
            if User.query.filter_by(referral_code=kwargs['referral_code']).first():
                return response_message(200, 'success', 'Valid referral code.')
        return response_message(401, 'fail', 'Invalid referral code.')

    @doc(
        description='Check Referral Code',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs({'ref': fields.Str()}, location="query")
    @marshal_with(RequestResponse)
    @TokenRequired
    def get(self, auth, **kwargs):
        """
        Using query parameter to send referral code
        """
        args = request.args
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        if user.referral_code != args.get('ref'):
            if User.query.filter_by(referral_code=args.get('ref')).first():
                return response_message(200, 'success', 'Valid referral code.')
        return response_message(401, 'fail', 'Invalid referral code.')
