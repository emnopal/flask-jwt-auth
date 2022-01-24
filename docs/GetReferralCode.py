from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import GetReferralCode
from helper.middleware import middleware


class GetReferralCodeResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Dict(required=True, description="Response for Referral Code")


class GetReferralCode(MethodResource, Resource):
    referral_code = GetReferralCode()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Find', 'Read', 'Get', 'Referral']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(GetReferralCodeResponse)
    @middleware
    def get(self, auth):
        return self.referral_code.get(auth)

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['Find', 'Read', 'Post', 'Referral']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(GetReferralCodeResponse)
    @middleware
    def post(self, auth):
        return self.get(auth)
