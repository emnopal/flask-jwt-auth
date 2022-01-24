from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import LogoutAPI
from middleware.must_login import must_login


class LogoutResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")


class LogoutAPI(MethodResource, Resource):
    logout = LogoutAPI()

    @doc(
        description='Log Out Endpoint.',
        tags=['Post', 'Logout']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    @must_login
    def post(self, auth):
        return self.logout.post(auth)

    @doc(
        description='Log Out Endpoint.',
        tags=['Get', 'Logout']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    @must_login
    def get(self, auth):
        return self.post(auth)

    @doc(
        description='Log Out Endpoint.',
        tags=['Delete', 'Logout']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    @must_login
    def delete(self, auth):
        return self.post(auth)