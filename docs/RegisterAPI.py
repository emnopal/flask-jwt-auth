from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import RegisterAPI


class RegisterRequest(Schema):
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")
    email = fields.Str(required=True, description="Input Field for Email, this is required and must be unique")
    name = fields.Str(required=True, description="Input Field for Name, this is required")


class RegisterResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Request method")


class RegisterAPI(MethodResource, Resource):
    register = RegisterAPI()

    @doc(description='Register Endpoint.', tags=['Create', 'Register', 'Post'])
    @use_kwargs(RegisterRequest, location='json')
    @marshal_with(RegisterResponse)
    def post(self):
        return self.register.post()