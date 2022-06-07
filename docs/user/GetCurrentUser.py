from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields
from controller import GetCurrentUser
from middleware import must_login


class GetCurrentUserResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(keys=fields.Str, values=fields.Str, description='Response data')


class GetCurrentUser(MethodResource, Resource):
    current_session = GetCurrentUser()

    @doc(description='Get Current Logged in User', tags=['Session', 'User'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(GetCurrentUserResponse)
    @must_login
    def get(self, auth):
        return self.current_session.get(auth)
