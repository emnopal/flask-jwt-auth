from marshmallow import Schema, fields
from model import User


class RequestResponse(Schema):
    fields_ = fields
    message = fields.Str(description=f"Response message")
    status = fields.Str(description="Response status")
    status_code = fields.Int(description="Response status code")
    method = fields.Str(description="Response request method")
    data = fields.Dict(keys=fields.Str, values=fields.Str, description='Response data')


class RequestPost(Schema):
    class Meta:
        model = User
    fields_ = fields
