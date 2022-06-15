from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields
from controller import GetUserByName
from middleware import must_login


class GetUserByNameResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(keys=fields.Str, values=fields.Str, description='Response data')


class GetUserByName(MethodResource, Resource):
    find_by_name = GetUserByName()

    @doc(
        description='Get Name of User Information Endpoint.',
        tags=['Session', 'User']
    )
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'name': fields.Str(description="Argument for find user by name"),
        'username': fields.Str(description="Argument for find user by username"),
        'mail': fields.Str(description="Argument for find user by email"),
    }, location='args')
    @marshal_with(GetUserByNameResponse)
    @must_login
    def get(self, auth):
        return self.find_by_name.get(auth)
