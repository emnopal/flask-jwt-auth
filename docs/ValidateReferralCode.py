from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import ValidateReferralCode
from middleware.must_login import must_login


class ValidateReferralCodeResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Str(description='Response data')


class ValidateReferralCodeRequest(Schema):
    referral_code = fields.Str(required=True, description="Input Field for Referral Code, this is required")


class ValidateReferralCode(MethodResource, Resource):
    valid_referral_code = ValidateReferralCode()

    @doc(
        description='Validated Referral Code, once ref code is validated, user can\'t use the ref code twice.',
        tags=['Referral']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(ValidateReferralCodeRequest, location='json')
    @marshal_with(ValidateReferralCodeResponse)
    @must_login
    def post(self, auth):
        return self.valid_referral_code.post(auth)

    @doc(
        description='Validated Referral Code, once ref code is validated, user can\'t use the ref code twice.',
        tags=['Referral']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'ref': fields.Str(required=True, description="Argument for validate referral code")
    }, location='args')
    @marshal_with(ValidateReferralCodeResponse)
    @must_login
    def get(self, auth):
        return self.valid_referral_code.get(auth)
