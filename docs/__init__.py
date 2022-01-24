from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from route import app

from flask_apispec import FlaskApiSpec
from werkzeug.utils import redirect
from flask_restful import Api

from docs.CurrentSession import CurrentSession
from docs.FindByName import FindByName
from docs.GetHeroName import GetHeroName
from docs.GetReferralCode import GetReferralCode
from docs.LoginAPI import LoginAPI
from docs.LogoutAPI import LogoutAPI
from docs.RegisterAPI import RegisterAPI
from docs.UpdatePassword import UpdatePassword
from docs.UpdateUserInformation import UpdateUserInformation
from docs.UpdateUsername import UpdateUsername
from docs.UserAPI import UserAPI
from docs.ValidateReferralCode import ValidateReferralCode

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask Authentication API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='3.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/docs/json',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/docs'  # URI to access UI of API Doc
})


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def redirect_to_json_api():
    return redirect('/docs/json')

docs = FlaskApiSpec(app)
api = Api(app)

api.add_resource(RegisterAPI, '/auth/register', methods=['POST'], endpoint='register_docs')
docs.register(RegisterAPI, endpoint='register_docs')

api.add_resource(LoginAPI, '/auth/login', methods=['POST'], endpoint='login_docs')
docs.register(LoginAPI, endpoint='login_docs')
api.add_resource(UserAPI, '/user', methods=['GET', 'POST'], endpoint='user_docs')
docs.register(UserAPI, endpoint='user_docs')
api.add_resource(FindByName, '/user/get', methods=['GET', 'POST'], endpoint='get_user_docs')
docs.register(FindByName, endpoint='get_user_docs')
api.add_resource(LogoutAPI, '/auth/logout', methods=['GET', 'POST', 'DELETE'], endpoint='logout_docs')
docs.register(LogoutAPI, endpoint='logout_docs')
api.add_resource(CurrentSession, '/session', methods=['GET', 'POST'], endpoint='session_docs')
docs.register(CurrentSession, endpoint='session_docs')
api.add_resource(UpdateUserInformation, '/user/update', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='docs_update_user_information')
docs.register(UpdateUserInformation, endpoint='docs_update_user_information')
api.add_resource(UpdatePassword, '/user/update/password', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='docs_update_password')
docs.register(UpdatePassword, endpoint='docs_update_password')
api.add_resource(
    UpdateUsername, '/user/update/username', methods=['POST', 'PUT', 'PATCH'], endpoint='docs_update_username')
docs.register(UpdateUsername, endpoint='docs_update_username')
api.add_resource(GetHeroName, '/hero', methods=['POST', 'GET'], endpoint='docs_hero')
docs.register(GetHeroName, endpoint='docs_hero')
api.add_resource(GetReferralCode, '/referral', methods=['POST', 'GET'], endpoint='referral_docs')
docs.register(GetReferralCode, endpoint='referral_docs')
api.add_resource(
    ValidateReferralCode, '/referral/validate', methods=['POST', 'GET'], endpoint='referral_validate_docs')
docs.register(ValidateReferralCode, endpoint='referral_validate_docs')

