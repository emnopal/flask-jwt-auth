from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from controller import GetHeroName
from middleware.must_login import must_login


class GetHeroResponse(Schema):
    message = fields.Str(description="Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(description="Response for Hero Name")


class GetHeroName(MethodResource, Resource):
    get_hero_name = GetHeroName()

    @doc(
        description='Get Hero Name and Properties Endpoint.',
        tags=['Hero']
    )
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'q': fields.Str(required=True, description="Argument for find hero by their name")
    }, location='args')
    @marshal_with(GetHeroResponse)
    @must_login
    def get(self, auth):
        return self.get_hero_name.get(auth)
