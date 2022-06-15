from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import CheckReferralCode
from middleware.must_login import must_login


class CheckReferralCodeResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Str(description='Response data')


class CheckReferralCodeRequest(Schema):
    referral_code = fields.Str(required=True, description="Input Field for Referral Code, this is required")


class CheckReferralCode(MethodResource, Resource):
    valid_referral_code = CheckReferralCode()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Referral']
    )
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(CheckReferralCodeRequest, location='json')
    @marshal_with(CheckReferralCodeResponse)
    @must_login
    def post(self, auth):
        return self.valid_referral_code.post(auth)

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Referral']
    )
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'ref': fields.Str(required=True, description="Argument for validate referral code")
    }, location='args')
    @marshal_with(CheckReferralCodeResponse)
    @must_login
    def get(self, auth):
        return self.valid_referral_code.get(auth)
