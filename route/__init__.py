from flask_restful import Api
from controller import app
from helper.message import response_message

from controller import RegisterAPI, LoginAPI, UserAPI, LogoutAPI, CurrentSession, UpdateUserInformation, \
    UpdatePassword, UpdateUsername, FindByName, GetHeroName, GetReferralCode, ValidateReferralCode

ENDPOINT = '/api'

api = Api(app)

@app.errorhandler(404)
def resource_not_found(e):
    return response_message(404, 'error', 'Resource not found', str(e))

api.add_resource(RegisterAPI, f'{ENDPOINT}/auth/register', methods=['POST'], endpoint='register')
api.add_resource(LoginAPI, f'{ENDPOINT}/auth/login', methods=['POST'], endpoint='login')
api.add_resource(UserAPI, f'{ENDPOINT}/user', methods=['GET'], endpoint='user')
api.add_resource(FindByName, f'{ENDPOINT}/user/get', methods=['GET'], endpoint='get_user')
api.add_resource(LogoutAPI, f'{ENDPOINT}/auth/logout', methods=['POST'], endpoint='logout')
api.add_resource(CurrentSession, f'{ENDPOINT}/session', methods=['GET'], endpoint='session')
api.add_resource(UpdateUserInformation, f'{ENDPOINT}/user/update', methods=['PATCH'], endpoint='update_user_information')
api.add_resource(UpdatePassword, f'{ENDPOINT}/user/update/password', methods=['PATCH'], endpoint='update_password')
api.add_resource(UpdateUsername, f'{ENDPOINT}/user/update/username', methods=['PATCH'], endpoint='update_username')
api.add_resource(GetHeroName, f'{ENDPOINT}/hero', methods=['GET'], endpoint='hero')
api.add_resource(GetReferralCode, f'{ENDPOINT}/referral', methods=['GET'], endpoint='referral')
api.add_resource(ValidateReferralCode, f'{ENDPOINT}/referral/validate', methods=['POST', 'GET'], endpoint='referral_validate')
