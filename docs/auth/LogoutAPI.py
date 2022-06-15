from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import LogoutAPI
from middleware.must_login import must_login


class LogoutResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")


class LogoutAPI(MethodResource, Resource):
    logout = LogoutAPI()

    @doc(
        description='Log Out Endpoint.',
        tags=['Session']
    )
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    @must_login
    def post(self, auth):
        return self.logout.post(auth)
