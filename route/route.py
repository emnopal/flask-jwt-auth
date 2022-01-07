from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from werkzeug.utils import redirect

from controller.controller import app, RegisterAPI, LoginAPI, UserAPI, LogoutAPI, CurrentSession, UpdateUserInformation, \
    UpdatePassword, UpdateUsername, FindByName, GetHeroName, GetReferralCode, ValidateReferralCode
from controller.controller_docs import RegisterAPIDocs, LoginAPIDocs, UserAPIDocs, FindByNameDocs, LogoutAPIDocs, \
    CurrentSessionDocs, UpdateUserInformationDocs, UpdatePasswordDocs, UpdateUsernameDocs, GetHeroNameDocs, \
    GetReferralCodeDocs, ValidateReferralCodeDocs

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


api = Api(app)
docs = FlaskApiSpec(app)

api.add_resource(RegisterAPI, '/auth/register', methods=['POST'], endpoint='register')
api.add_resource(RegisterAPIDocs, '/auth/register', methods=['POST'], endpoint='register_docs')
docs.register(RegisterAPIDocs, endpoint='register_docs')

api.add_resource(LoginAPI, '/auth/login', methods=['GET', 'POST'], endpoint='login')
api.add_resource(LoginAPIDocs, '/auth/login', methods=['POST'], endpoint='login_docs')
docs.register(LoginAPIDocs, endpoint='login_docs')

api.add_resource(UserAPI, '/user', methods=['GET', 'POST'], endpoint='user')
api.add_resource(UserAPIDocs, '/user', methods=['GET', 'POST'], endpoint='user_docs')
docs.register(UserAPIDocs, endpoint='user_docs')

api.add_resource(FindByName, '/user/get', methods=['GET', 'POST'], endpoint='get_user')
api.add_resource(FindByNameDocs, '/user/get', methods=['GET', 'POST'], endpoint='get_user_docs')
docs.register(FindByNameDocs, endpoint='get_user_docs')

api.add_resource(LogoutAPI, '/auth/logout', methods=['GET', 'POST', 'DELETE'], endpoint='logout')
api.add_resource(LogoutAPIDocs, '/auth/logout', methods=['GET', 'POST', 'DELETE'], endpoint='logout_docs')
docs.register(LogoutAPIDocs, endpoint='logout_docs')

api.add_resource(CurrentSession, '/session', methods=['GET', 'POST'], endpoint='session')
api.add_resource(CurrentSessionDocs, '/session', methods=['GET', 'POST'], endpoint='session_docs')
docs.register(CurrentSessionDocs, endpoint='session_docs')

api.add_resource(UpdateUserInformation, '/user/update', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='update_user_information')
api.add_resource(UpdateUserInformationDocs, '/user/update', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='docs_update_user_information')
docs.register(UpdateUserInformationDocs, endpoint='docs_update_user_information')

api.add_resource(UpdatePassword, '/user/update/password', methods=['POST', 'PUT', 'PATCH'], endpoint='update_password')
api.add_resource(UpdatePasswordDocs, '/user/update/password', methods=['POST', 'PUT', 'PATCH'],
                 endpoint='docs_update_password')
docs.register(UpdatePasswordDocs, endpoint='docs_update_password')

api.add_resource(UpdateUsername, '/user/update/username', methods=['POST', 'PUT', 'PATCH'], endpoint='update_username')
api.add_resource(
    UpdateUsernameDocs, '/user/update/username', methods=['POST', 'PUT', 'PATCH'], endpoint='docs_update_username')
docs.register(UpdateUsernameDocs, endpoint='docs_update_username')

api.add_resource(GetHeroName, '/hero', methods=['POST', 'GET'], endpoint='hero')
api.add_resource(GetHeroNameDocs, '/hero', methods=['POST', 'GET'], endpoint='docs_hero')
docs.register(GetHeroNameDocs, endpoint='docs_hero')

api.add_resource(GetReferralCode, '/referral', methods=['POST', 'GET'], endpoint='referral')
api.add_resource(GetReferralCodeDocs, '/referral', methods=['POST', 'GET'], endpoint='referral_docs')
docs.register(GetReferralCodeDocs, endpoint='referral_docs')

api.add_resource(ValidateReferralCode, '/referral/validate', methods=['POST', 'GET'], endpoint='referral_validate')
api.add_resource(
    ValidateReferralCodeDocs, '/referral/validate', methods=['POST', 'GET'], endpoint='referral_validate_docs')
docs.register(ValidateReferralCodeDocs, endpoint='referral_validate_docs')
