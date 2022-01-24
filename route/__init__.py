from flask_restful import Api
from controller import app
from helper.message import response_message

from controller import RegisterAPI, LoginAPI, UserAPI, LogoutAPI, CurrentSession, UpdateUserInformation, \
    UpdatePassword, UpdateUsername, FindByName, GetHeroName, GetReferralCode, ValidateReferralCode

api = Api(app)

@app.errorhandler(404)
def resource_not_found(e):
    return response_message(404, 'error', 'Resource not found', str(e))

api.add_resource(RegisterAPI, '/auth/register', methods=['POST'], endpoint='register')
api.add_resource(LoginAPI, '/auth/login', methods=['GET', 'POST'], endpoint='login')
api.add_resource(UserAPI, '/user', methods=['GET', 'POST'], endpoint='user')
api.add_resource(FindByName, '/user/get', methods=['GET', 'POST'], endpoint='get_user')
api.add_resource(LogoutAPI, '/auth/logout', methods=['GET', 'POST', 'DELETE'], endpoint='logout')
api.add_resource(CurrentSession, '/session', methods=['GET', 'POST'], endpoint='session')
api.add_resource(UpdateUserInformation, '/user/update', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='update_user_information')
api.add_resource(UpdatePassword, '/user/update/password', methods=['POST', 'PUT', 'PATCH'], endpoint='update_password')
api.add_resource(UpdateUsername, '/user/update/username', methods=['POST', 'PUT', 'PATCH'], endpoint='update_username')
api.add_resource(GetHeroName, '/hero', methods=['POST', 'GET'], endpoint='hero')
api.add_resource(GetReferralCode, '/referral', methods=['POST', 'GET'], endpoint='referral')
api.add_resource(ValidateReferralCode, '/referral/validate', methods=['POST', 'GET'], endpoint='referral_validate')
