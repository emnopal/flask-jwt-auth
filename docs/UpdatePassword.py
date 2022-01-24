from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import UpdatePassword
from helper.middleware import middleware


class UpdatePasswordRequest(Schema):
    username = fields.Str(required=True, description="Input Field for Name, this is required")
    old_password = fields.Str(required=True, description="Input Field for Old Password, this is required")
    new_password = fields.Str(required=True, description="Input Field for New Password, this is required")


class UpdatePasswordResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")


class UpdatePassword(MethodResource, Resource):
    update_password = UpdatePassword()

    @doc(description='Update User Password Endpoint.', tags=['Update', 'Password', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    @middleware
    def post(self, auth):
        return self.update_password.post(auth)

    @doc(description='Update User Password Endpoint.', tags=['Update', 'Password', 'Put', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    @middleware
    def put(self, auth):
        return self.post(auth)

    @doc(description='Update User Password Endpoint.', tags=['Update', 'Password', 'Patch', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    @middleware
    def patch(self, auth):
        return self.post(auth)
