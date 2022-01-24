from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import BlacklistToken
from controller import db
from helper.middleware import middleware


class LogoutAPI(MethodResource, Resource):

    @middleware
    def post(self, auth):
        blacklist_token = BlacklistToken(token=auth['auth_header'])
        try:
            db.session.add(blacklist_token)
            db.session.commit()
            res = response_message(200, 'success', 'Successfully logged out.')
            res.set_cookie('app_session', '', expires=0)
            return res
        except Exception as e:
            return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')

    @middleware
    def get(self, auth):
        return self.post(auth)

    @middleware
    def delete(self, auth):
        return self.post(auth)
