from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields
from flask import request
from marshmallow import Schema, fields

from controller import CurrentSession


class CurrentSessionData(Schema):
    auth_token = fields.Str(required=True, description="Response for Auth Token after Login")
    decoded_token = fields.Str(required=True, description="Response for decoded token if query decode is true")


class CurrentSessionResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")
    data = fields.Nested(CurrentSessionData())


class CurrentSession(MethodResource, Resource):
    current_session = CurrentSession()

    @doc(description='Current Session Endpoint.', tags=['Read', 'Session', 'Get'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'decode': fields.Str(required=True, description="Argument from URL for decoded JWT", default=None)
    }, location='args')
    @marshal_with(CurrentSessionResponse)
    def get(self):
        return self.current_session.get()

    @doc(description='Current Session Endpoint.', tags=['Read', 'Session', 'Post'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'decode': fields.Str(required=True, description="Argument from URL for decoded JWT", default=None)
    }, location='args')
    @marshal_with(CurrentSessionResponse)
    def post(self):
        return self.get()