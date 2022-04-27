from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import LoginAPI


class LoginRequestPost(Schema):
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class LoginRequestGet(Schema):
    cookies = fields.Str(required=True, description="Authorization JWT from cookies")


class LoginResponseData(Schema):
    auth_token = fields.Str(required=True, description="Response for Auth Token after Login")
    referral_code = fields.Str(required=True, description="Response for Referral Code after Login")


class LoginResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Nested(LoginResponseData())


class LoginAPI(MethodResource, Resource):
    login = LoginAPI()

    @doc(description='Login Endpoint.', tags=['Session'])
    @use_kwargs(LoginRequestPost, location='json')
    @marshal_with(LoginResponse)
    def post(self):
        return self.login.post()
