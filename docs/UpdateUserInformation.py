from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import UpdateUserInformation


class UpdateUserInformationRequest(Schema):
    name = fields.Str(required=True, description="Input Field for Name, this is required")
    email = fields.Str(required=True, description="Input Field for Email, this is required and must be unique")
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class UpdateUserInformationResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")


class UpdateUserInformation(MethodResource, Resource):
    update_user_information = UpdateUserInformation()

    @doc(description='Update User Information Endpoint.', tags=['Update', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUserInformationRequest, location='json')
    @marshal_with(UpdateUserInformationResponse)
    def post(self):
        return self.update_user_information.post()

    @doc(description='Update User Information Endpoint.', tags=['Update', 'Put', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUserInformationRequest, location='json')
    @marshal_with(UpdateUserInformationResponse)
    def put(self):
        return self.post()

    @doc(description='Update User Information Endpoint.', tags=['Update', 'Patch', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUserInformationRequest, location='json')
    @marshal_with(UpdateUserInformationResponse)
    def patch(self):
        return self.post()