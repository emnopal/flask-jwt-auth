from flask import request
from marshmallow import Schema, fields


# Register Docs
class RegisterRequest(Schema):
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")
    email = fields.Str(required=True, description="Input Field for Email, this is required and must be unique")
    name = fields.Str(required=True, description="Input Field for Name, this is required")


class RegisterResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Request method")


# Login Docs
class LoginRequestPost(Schema):
    username = fields.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class LoginRequestGet(Schema):
    cookies = fields.Str(required=True, description="Authorization JWT from cookies")


class LoginResponseData(Schema):
    auth_token = fields.Str(required=True, description="Response for Auth Token after Login")
    referral_code = fields.Str(required=True, description="Response for Referral Code after Login")


class LoginResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Nested(LoginResponseData())


class CurrentSessionData(Schema):
    auth_token = fields.Str(required=True, description="Response for Auth Token after Login")
    decoded_token = fields.Str(required=True, description="Response for decoded token if query decode is true")


class CurrentSessionResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")
    data = fields.Nested(CurrentSessionData())


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


class UpdatePasswordRequest(Schema):
    username = fields.Str(required=True, description="Input Field for Name, this is required")
    old_password = fields.Str(required=True, description="Input Field for Old Password, this is required")
    new_password = fields.Str(required=True, description="Input Field for New Password, this is required")


class UpdatePasswordResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")


class NewSessionData(Schema):
    new_auth_token = fields.Str(required=True, description="Response for New Auth Token after Change Username")


class UpdateUsernameRequest(Schema):
    old_username = fields.Str(required=True, description="Input Field for Old Name, this is required")
    new_username = fields.Str(required=True, description="Input Field for New Username, this is required")
    password = fields.Str(required=True, description="Input Field for Password, this is required")


class UpdateUsernameResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="GET", description="Response request method")
    data = fields.Nested(NewSessionData())


class UserResponseData(Schema):
    username = fields.Str(required=True, description="Response for Username")
    name = fields.Str(required=True, description="Response for Name")
    email = fields.Str(required=True, description="Response for Email")
    registered_on = fields.DateTime(required=True, description="Response for Registered On (Time)")
    referral_code = fields.Str(required=True, description="Response for Referral Code")


class UserResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Nested(UserResponseData())


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


class GetReferralCodeResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Dict(required=True, description="Response for Referral Code")


class ValidateReferralCodeResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")


class ValidateReferralCodeRequest(Schema):
    referral_code = fields.Str(required=True, description="Input Field for Referral Code, this is required")


class GetHeroResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")
    data = fields.Dict(required=True, description="Response for Hero Name")


class LogoutResponse(Schema):
    message = fields.Str(required=True, description="Response message")
    status = fields.Str(required=True, description="Response status")
    status_code = fields.Int(required=True, description="Response status code")
    method = fields.Str(required=True, default="POST", description="Response request method")