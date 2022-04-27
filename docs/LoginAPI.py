from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from marshmallow import Schema, fields
from controller import LoginAPI


class LoginRequestPost(Schema):
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class LoginResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(keys=fields.Str, values=fields.Str, description='Response data')


class LoginAPI(MethodResource, Resource):
    login = LoginAPI()
    @doc(description='Login Endpoint.', tags=['Session'])
    @use_kwargs(LoginRequestPost, location='json')
    @marshal_with(LoginResponse)
    def post(self):
        return self.login.post()
