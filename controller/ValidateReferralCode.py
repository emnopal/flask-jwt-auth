from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from flask_restful import Resource
from helper import response_message, RequestResponse, RequestPost
from middleware import TokenRequired
from model import User, db


class ValidateReferralCodeRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    referral_code = fields_.Str(required=True, description="Input Field for Referral Code, this is required")


class ValidateReferralCode(MethodResource):
    fields = ValidateReferralCodeRequestPost.fields_

    @doc(
        description='Validate Referral Code',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(ValidateReferralCodeRequestPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        print(kwargs['referral_code'])
        """
        Using json to send referral code
        """
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        if user.referral_code != kwargs['referral_code']:
            if User.query.filter_by(referral_code=kwargs['referral_code']).first():
                if not user.redeemed_referral_code:
                    try:
                        user.redeemed_referral_code = kwargs['referral_code']
                        db.session.commit()
                    except Exception as e:
                        return response_message(500, 'fail', f'Error Occured {e}')
                    return response_message(200, 'success', 'Referral code is redeemed')
                else:
                    return response_message(401, 'fail', 'You have redeemed referral code before')
        return response_message(401, 'fail', 'Invalid referral code.')

    @doc(
        description='Validate Referral Code',
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
    def get(self, auth):
        """
        Using query parameter to send referral code
        """
        args = request.args
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        if user.referral_code != args.get('ref'):
            if User.query.filter_by(referral_code=args.get('ref')).first():
                if not user.redeemed_referral_code:
                    try:
                        user.redeemed_referral_code = args.get('ref')
                        db.session.commit()
                    except Exception as e:
                        return response_message(500, 'fail', f'Error Occurred {e}')
                    return response_message(200, 'success', 'Referral code is redeemed')
                else:
                    return response_message(401, 'fail', 'You have redeemed referral code before')
        return response_message(401, 'fail', 'Invalid referral code.')
