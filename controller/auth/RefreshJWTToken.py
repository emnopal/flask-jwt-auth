from flask_apispec import MethodResource, marshal_with, doc
from helper import response_message, Auth, RequestResponse
from model import BlacklistToken, User
from controller import db
from middleware import TokenRequired


class RefreshJWTToken(MethodResource):

    @doc(
        description='Refresh Token Endpoint.',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @marshal_with(RequestResponse)
    @TokenRequired
    def get(self, auth, **kwargs):
        blacklist_token = BlacklistToken(token=auth['auth_header'])
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        try:
            db.session.add(blacklist_token)
            auth_token_data = {
                'username': str(user.username)
            }
            new_auth_token = Auth(data=auth_token_data).EncodeAuthToken()
            db.session.commit()
            data = {
                'new_auth_token': new_auth_token,
            }
            return response_message(200, 'success', 'New Auth Token', data)
        except Exception:
            return response_message(500, 'fail', 'Internal Server Error')
