import datetime
from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse
from model import BlacklistToken, User
from controller import db
from middleware import TokenRequired


class LogoutResponse(RequestResponse):
    fields_ = RequestResponse.fields_
    data = fields_.Constant(constant=None, description='Response data')


class LogoutAPI(MethodResource):

    # From this, started from 2013, only post that make sense for logout method: https://stackoverflow.com/a/14587231
    @doc(
        description='Logout Endpoint.',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @marshal_with(LogoutResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        blacklist_token = BlacklistToken(token=auth['auth_header'])
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        try:
            db.session.add(blacklist_token)
            user.last_logged_in = None
            user.last_logged_out = datetime.datetime.now()
            db.session.commit()
            return response_message(200, 'success', 'Successfully logged out.')
        except Exception as e:
            return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')
