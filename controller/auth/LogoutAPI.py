import datetime
from flask_apispec import MethodResource
from flask_restful import Resource
from helper import response_message
from model import BlacklistToken, User
from controller import db, app
from middleware import must_login


class LogoutAPI(MethodResource, Resource):

    # From this, started from 2013, only post that make sense for logout method: https://stackoverflow.com/a/14587231
    @must_login
    def post(self, auth):
        blacklist_token = BlacklistToken(token=auth['auth_header'])
        user = User.query.filter_by(username=auth['resp']['sub']['username']).first()
        try:
            db.session.add(blacklist_token)
            user.last_logged_in = None
            user.last_logged_out = datetime.datetime.now()
            db.session.commit()
            res = response_message(200, 'success', 'Successfully logged out.')
            res.set_cookie(app.config.get('COOKIE_NAME'), '', expires=0)
            return res
        except Exception as e:
            return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')

