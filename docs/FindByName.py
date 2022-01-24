from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import FindByName

class GetNameResponseData(Schema):
    username = fields.Str(required=True, description="Response for Username")
    name = fields.Str(required=True, description="Response for Name")
    email = fields.Str(required=True, description="Response for Email")


class GetNameResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Nested(GetNameResponseData())


class FindByName(MethodResource, Resource):
    find_by_name = FindByName()

    @doc(
        description='Get Name of User Information Endpoint.',
        tags=['Find', 'Read', 'Get', 'Profile']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'name': fields.Str(required=True, description="Argument for find user by name")
    }, location='args')
    @marshal_with(GetNameResponse)
    def get(self):
        return self.find_by_name.get()

    @doc(
        description='Get Name of User Information Endpoint.',
        tags=['Find', 'Read', 'Post', 'Profile']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'name': fields.Str(required=True, description="Argument for find user by name")
    }, location='args')
    @marshal_with(GetNameResponse)
    def post(self):
        return self.get()