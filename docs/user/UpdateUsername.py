from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields
from controller import UpdateUsername
from middleware.must_login import must_login


class UpdateUsernameRequest(Schema):
    old_username = fields.Str(required=True, description="Input Field for Old Name, this is required")
    new_username = fields.Str(required=True, description="Input Field for New Username, this is required")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class UpdateUsernameResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(keys=fields.Str, values=fields.Str, description='Response data')


class UpdateUsername(MethodResource, Resource):
    update_username = UpdateUsername()

    @doc(description='Update Username Endpoint.', tags=['Session', 'Username', 'User'])
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    @must_login
    def patch(self, auth):
        return self.post(auth)