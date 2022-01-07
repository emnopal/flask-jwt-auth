from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from flask_restful import Resource
from marshmallow import fields

from controller.controller import RegisterAPI, LoginAPI, CurrentSession, UpdateUserInformation, UpdatePassword, \
    UpdateUsername, UserAPI, FindByName, GetHeroName, LogoutAPI, GetReferralCode, ValidateReferralCode
from helper.docs import RegisterRequest, RegisterResponse, LoginRequestPost, LoginResponse, LoginRequestGet, \
    CurrentSessionResponse, UpdateUserInformationRequest, UpdateUserInformationResponse, UpdatePasswordRequest, \
    UpdatePasswordResponse, UpdateUsernameRequest, UpdateUsernameResponse, UserResponse, GetNameResponse, \
    LogoutResponse, GetHeroResponse, GetReferralCodeResponse, ValidateReferralCodeResponse, ValidateReferralCodeRequest


class RegisterAPIDocs(MethodResource, Resource):
    register = RegisterAPI()

    @doc(description='Register Endpoint.', tags=['Register', 'Login', 'Post'])
    @use_kwargs(RegisterRequest, location='json')
    @marshal_with(RegisterResponse)
    def post(self):
        return self.register.post()


class LoginAPIDocs(MethodResource, Resource):
    login = LoginAPI()

    @doc(description='Login Endpoint.', tags=['Login', 'Post'])
    @use_kwargs(LoginRequestPost, location='json')
    @marshal_with(LoginResponse)
    def post(self):
        return self.login.post()

    @doc(description='Login Endpoint.', tags=['Login', 'Get', 'Session', 'Token'])
    @use_kwargs(LoginRequestGet, location='cookies')
    @marshal_with(LoginResponse)
    def get(self):
        return self.login.get()


class CurrentSessionDocs(MethodResource, Resource):
    current_session = CurrentSession()

    @doc(description='Current Session Endpoint.', tags=['Session', 'Login', 'Token', 'Get'])
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

    @doc(description='Current Session Endpoint.', tags=['Session', 'Login', 'Token', 'Post'])
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


class UpdateUserInformationDocs(MethodResource, Resource):
    update_user_information = UpdateUserInformation()

    @doc(description='Update User Information Endpoint.', tags=['User', 'Update', 'Post', 'Profile'])
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

    @doc(description='Update User Information Endpoint.', tags=['User', 'Update', 'Put', 'Profile'])
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

    @doc(description='Update User Information Endpoint.', tags=['User', 'Update', 'Patch', 'Profile'])
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


class UpdatePasswordDocs(MethodResource, Resource):
    update_password = UpdatePassword()

    @doc(description='Update User Password Endpoint.', tags=['User', 'Update', 'Password', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    def post(self):
        return self.update_password.post()

    @doc(description='Update User Password Endpoint.', tags=['User', 'Update', 'Password', 'Put', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    def put(self):
        return self.post()

    @doc(description='Update User Password Endpoint.', tags=['User', 'Update', 'Password', 'Patch', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdatePasswordRequest, location='json')
    @marshal_with(UpdatePasswordResponse)
    def patch(self):
        return self.post()


class UpdateUsernameDocs(MethodResource, Resource):
    update_username = UpdateUsername()

    @doc(description='Update Username Endpoint.', tags=['User', 'Update', 'Username', 'Post', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    def post(self):
        return self.update_username.post()

    @doc(description='Update Username Endpoint.', tags=['User', 'Update', 'Username', 'Put', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    def put(self):
        return self.post()

    @doc(description='Update Username Endpoint.', tags=['User', 'Update', 'Username', 'Patch', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(UpdateUsernameRequest, location='json')
    @marshal_with(UpdateUsernameResponse)
    def patch(self):
        return self.post()


class UserAPIDocs(MethodResource, Resource):
    get_user = UserAPI()

    @doc(description='Get User Information Endpoint.', tags=['User', 'Get', 'Username', 'Session', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(UserResponse)
    def get(self):
        return self.get_user.get()

    @doc(description='Get User Information Endpoint.', tags=['User', 'Post', 'Username', 'Session', 'Profile'])
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(UserResponse)
    def post(self):
        return self.get()


class FindByNameDocs(MethodResource, Resource):
    find_by_name = FindByName()

    @doc(
        description='Get Name of User Information Endpoint.',
        tags=['User', 'Get', 'Name', 'Session', 'Profile', 'Find']
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
        tags=['User', 'Post', 'Name', 'Session', 'Profile', 'Find']
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


class GetReferralCodeDocs(MethodResource, Resource):
    referral_code = GetReferralCode()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['User', 'Get', 'Name', 'Session', 'Profile', 'Find', 'Referral', 'Code']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(GetReferralCodeResponse)
    def get(self):
        return self.referral_code.get()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['User', 'Post', 'Name', 'Session', 'Profile', 'Find', 'Referral', 'Code']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(GetReferralCodeResponse)
    def post(self):
        return self.get()


class ValidateReferralCodeDocs(MethodResource, Resource):
    valid_referral_code = ValidateReferralCode()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['User', 'Post', 'Name', 'Session', 'Profile', 'Validate', 'Referral', 'Code']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs(ValidateReferralCodeRequest, location='json')
    @marshal_with(ValidateReferralCodeResponse)
    def post(self):
        return self.valid_referral_code.post()

    @doc(
        description='Get Referral Code of User Information Endpoint.',
        tags=['User', 'Get', 'Name', 'Session', 'Profile', 'Validate', 'Referral', 'Code']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'ref': fields.Str(required=True, description="Argument for validate referral code")
    }, location='args')
    @marshal_with(ValidateReferralCodeResponse)
    def get(self):
        return self.valid_referral_code.get()


class GetHeroNameDocs(MethodResource, Resource):
    get_hero_name = GetHeroName()

    @doc(
        description='Get Hero Name and Properties Endpoint.',
        tags=['Hero', 'Get', 'Name', 'Find']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'q': fields.Str(required=True, description="Argument for find hero by their name")
    }, location='args')
    @marshal_with(GetHeroResponse)
    def get(self):
        return self.get_hero_name.get()

    @doc(
        description='Get Name of User Information Endpoint.',
        tags=['User', 'Post', 'Name', 'Session', 'Profile', 'Find']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @use_kwargs({
        'q': fields.Str(required=True, description="Argument for find hero by name")
    }, location='args')
    @marshal_with(GetHeroResponse)
    def post(self):
        return self.get()


class LogoutAPIDocs(MethodResource, Resource):
    logout = LogoutAPI()

    @doc(
        description='Log Out Endpoint.',
        tags=['Post', 'Session', 'Login', 'Logout', 'Register', 'Token']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    def post(self):
        return self.logout.post()

    @doc(
        description='Log Out Endpoint.',
        tags=['Get', 'Session', 'Login', 'Logout', 'Register', 'Token']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    def get(self):
        return self.post()

    @doc(
        description='Log Out Endpoint.',
        tags=['Delete', 'Session', 'Login', 'Logout', 'Register', 'Token']
    )
    @use_kwargs({
        'cookies': fields.Str(required=True, description="Authorization JWT from cookies")
    }, location='cookies')
    @use_kwargs({
        'headers': fields.Str(required=True, description="Authorization HTTP header with JWT refresh token")
    }, location='headers')
    @marshal_with(LogoutResponse)
    def delete(self):
        return self.post()
