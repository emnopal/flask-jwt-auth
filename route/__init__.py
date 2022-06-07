from flask_restful import Api
from helper import response_message

from controller import (
    app,
    RegisterAPI,
    LoginAPI,
    LogoutAPI,
    UpdateUserInformation,
    UpdatePassword,
    UpdateUsername,
    GetHeroName,
    ValidateReferralCode,
    GetCurrentUser,
    GetUserByName,
    CheckReferralCode,
    RefreshJWTToken
)


ENDPOINT = app.config.get('APP_PREFIX')

api = Api(app)

@app.errorhandler(404)
def resource_not_found(e):
    return response_message(404, 'error', 'Resource not found', str(e))

api.add_resource(RegisterAPI, f'{ENDPOINT}/auth/register', methods=['POST'], endpoint='Register')
api.add_resource(LoginAPI, f'{ENDPOINT}/auth/login', methods=['POST'], endpoint='Login')
api.add_resource(LogoutAPI, f'{ENDPOINT}/auth/logout', methods=['POST'], endpoint='Logout')

api.add_resource(GetCurrentUser, f'{ENDPOINT}/auth/user', methods=['GET'], endpoint='GetAuthUser')
api.add_resource(RefreshJWTToken, f'{ENDPOINT}/auth/refresh', methods=['GET'], endpoint='RefreshJWTToken')
api.add_resource(UpdateUserInformation, f'{ENDPOINT}/auth/user', methods=['PATCH'], endpoint='UpdateAuthUserInfo')
api.add_resource(UpdatePassword, f'{ENDPOINT}/auth/user/password', methods=['PATCH'], endpoint='UpdateAuthPassword')
api.add_resource(UpdateUsername, f'{ENDPOINT}/auth/user/username', methods=['PATCH'], endpoint='UpdateAuthUsername')

api.add_resource(GetUserByName, f'{ENDPOINT}/user', methods=['GET'], endpoint='GetUser')
api.add_resource(GetHeroName, f'{ENDPOINT}/hero', methods=['GET'], endpoint='GetHero')
api.add_resource(CheckReferralCode, f'{ENDPOINT}/referral', methods=['POST', 'GET'], endpoint='CheckReferralCode')
api.add_resource(ValidateReferralCode, f'{ENDPOINT}/referral/validate', methods=['POST', 'GET'], endpoint='ValidateReferralCode')
