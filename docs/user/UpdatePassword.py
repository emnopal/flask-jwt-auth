from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import UpdatePassword
from middleware.must_login import must_login


class UpdatePasswordRequest(Schema):
    username = fields.Str(required=True, description="Input Field for Name, this is required")
    old_password = fields.Str(required=True, description="Input Field for Old Password, this is required")
    new_password = fields.Str(required=True, description="Input Field for New Password, this is required")


class UpdatePasswordResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")


class UpdatePassword(MethodResource, Resource):
    update_password = UpdatePassword()

    @doc(description='Update User Password Endpoint.', tags=['Session', 'Password', 'User'])
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    @must_login
    def patch(self, auth):
        return self.post(auth)
