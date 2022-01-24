from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import ValidateReferralCode


class ValidateReferralCodeResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")


class ValidateReferralCodeRequest(Schema):
    referral_code = fields.Str(required=True, description="Input Field for Referral Code, this is required")


class ValidateReferralCode(MethodResource, Resource):
    valid_referral_code = ValidateReferralCode()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Validate', 'Read', 'Post', 'Referral']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(ValidateReferralCodeRequest, location='json')
    @marshal_with(ValidateReferralCodeResponse)
    def post(self):
        return self.valid_referral_code.post()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Validate', 'Read', 'Get', 'Referral']
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
    def get(self):
        return self.valid_referral_code.get()