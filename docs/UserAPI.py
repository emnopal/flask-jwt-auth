from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import UserAPI
from helper.middleware import middleware


class UserResponseData(Schema):
    username = fields.Str(required=True, description="Response for Username")
    name = fields.Str(required=True, description="Response for Name")
    email = fields.Str(required=True, description="Response for Email")
    registered_on = fields.DateTime(required=True, description="Response for Registered On (Time)")
    referral_code = fields.Str(required=True, description="Response for Referral Code")


class UserResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Nested(UserResponseData())


class UserAPI(MethodResource, Resource):
    get_user = UserAPI()

    @doc(description='Get User Information Endpoint.', tags=['Read', 'Get', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(UserResponse)
    @middleware
    def get(self, auth):
        return self.get_user.get(auth)

    @doc(description='Get User Information Endpoint.', tags=['Read', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(UserResponse)
    @middleware
    def post(self, auth):
        return self.get(auth)