import datetime
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message, encode_auth_token
from model import BlacklistToken, User
from controller import db, app
from middleware import must_login


class RefreshJWTToken(MethodResource, Resource):

    @must_login
    def get(self, auth):
        conf = app.config
        blacklist_token = BlacklistToken(token=auth['auth_header'])
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        try:
            db.session.add(blacklist_token)
            new_auth_token = encode_auth_token(user.username, int(conf.get('TOKEN_EXPIRED')))
            db.session.commit()
            data = {
                'new_auth_token': new_auth_token,
            }
            return response_message(200, 'success', 'New Auth Token', data)
        except Exception as e:
            return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')

