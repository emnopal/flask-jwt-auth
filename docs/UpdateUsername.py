from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import UpdateUsername
from middleware.must_login import must_login


class NewSessionData(Schema):
    new_auth_token = fields.Str(required=True, description="Response for New Auth Token after Change Username")


class UpdateUsernameRequest(Schema):
    old_username = fields.Str(required=True, description="Input Field for Old Name, this is required")
    new_username = fields.Str(required=True, description="Input Field for New Username, this is required")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class UpdateUsernameResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")
    data = fields.Nested(NewSessionData())


class UpdateUsername(MethodResource, Resource):
    update_username = UpdateUsername()

    @doc(description='Update Username Endpoint.', tags=['Update', 'Username', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    @must_login
    def post(self, auth):
        return self.update_username.post(auth)

    @doc(description='Update Username Endpoint.', tags=['Update', 'Username', 'Put', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    @must_login
    def put(self, auth):
        return self.post(auth)

    @doc(description='Update Username Endpoint.', tags=['Update', 'Username', 'Patch', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    @must_login
    def patch(self, auth):
        return self.post(auth)