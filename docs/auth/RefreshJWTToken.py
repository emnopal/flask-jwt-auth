from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import RefreshJWTToken
from middleware.must_login import must_login


class RefreshJWTTokenResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")


class RefreshJWTToken(MethodResource, Resource):
    refresh = RefreshJWTToken()

    @doc(
        description='Refresh Endpoint.',
        tags=['Session']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(RefreshJWTTokenResponse)
    @must_login
    def post(self, auth):
        return self.refresh.post(auth)
