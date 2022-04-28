from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from route import app

from flask_apispec import FlaskApiSpec
from werkzeug.utils import redirect
from flask_restful import Api

from docs.GetCurrentUser import GetCurrentUser
from docs.GetHeroName import GetHeroName
from docs.LoginAPI import LoginAPI
from docs.LogoutAPI import LogoutAPI
from docs.RegisterAPI import RegisterAPI
from docs.UpdatePassword import UpdatePassword
from docs.UpdateUserInformation import UpdateUserInformation
from docs.UpdateUsername import UpdateUsername
from docs.ValidateReferralCode import ValidateReferralCode
from docs.GetUserByName import GetUserByName
from docs.CheckReferralCode import CheckReferralCode

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

ENDPOINT_DOCS = app.config.get('APP_PREFIX')

@app.route('/', methods=['GET', 'POST', 'PATCH'])
@app.route('/api', methods=['GET', 'POST', 'PATCH'])
def redirect_to_json_api():
    return redirect(f'/docs/json')

docs = FlaskApiSpec(app)
api = Api(app)

api.add_resource(RegisterAPI, f'{ENDPOINT_DOCS}/auth/register', methods=['POST'], endpoint='DocsRegister')
docs.register(RegisterAPI, endpoint='DocsRegister')

api.add_resource(LoginAPI, f'{ENDPOINT_DOCS}/auth/login', methods=['POST'], endpoint='DocsLogin')
docs.register(LoginAPI, endpoint='DocsLogin')

api.add_resource(LogoutAPI, f'{ENDPOINT_DOCS}/auth/logout', methods=['POST'], endpoint='DocsLogout')
docs.register(LogoutAPI, endpoint='DocsLogout')

api.add_resource(GetCurrentUser, f'{ENDPOINT_DOCS}/auth/user', methods=['GET'], endpoint='DocsGetAuthUser')
docs.register(GetCurrentUser, endpoint='DocsGetAuthUser')

api.add_resource(UpdateUserInformation, f'{ENDPOINT_DOCS}/auth/user', methods=['PATCH'], endpoint='DocsUpdateAuthUserInfo')
docs.register(UpdateUserInformation, endpoint='DocsUpdateAuthUserInfo')

api.add_resource(UpdatePassword, f'{ENDPOINT_DOCS}/auth/user/password', methods=['PATCH'], endpoint='DocsUpdateAuthPassword')
docs.register(UpdatePassword, endpoint='DocsUpdateAuthPassword')

api.add_resource(UpdateUsername, f'{ENDPOINT_DOCS}/auth/user/username', methods=['PATCH'], endpoint='DocsUpdateAuthUsername')
docs.register(UpdateUsername, endpoint='DocsUpdateAuthUsername')

api.add_resource(GetUserByName, f'{ENDPOINT_DOCS}/user', methods=['GET'], endpoint='DocsGetUserByName')
docs.register(GetUserByName, endpoint='DocsGetUserByName')

api.add_resource(GetHeroName, f'{ENDPOINT_DOCS}/hero', methods=['GET'], endpoint='DocsGetHero')
docs.register(GetHeroName, endpoint='DocsGetHero')

api.add_resource(CheckReferralCode, f'{ENDPOINT_DOCS}/referral', methods=['POST', 'GET'], endpoint='DocsCheckReferralCode')
docs.register(CheckReferralCode, endpoint='DocsCheckReferralCode')

api.add_resource(ValidateReferralCode, f'{ENDPOINT_DOCS}/referral/validate', methods=['POST', 'GET'], endpoint='DocsValidateReferralCode')
docs.register(ValidateReferralCode, endpoint='DocsValidateReferralCode')

