from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from helper.middleware import middleware


class CurrentSession(MethodResource, Resource):

    @middleware
    def get(self, auth):
        args = request.args
        if args.get('decode') in ['true', 'True', 1, '1']:
            data = {
                'auth_token': auth['auth_cookie'],
                'decoded_token': auth['resp'],
            }
            return response_message(200, 'success', 'Successfully get session data.', data)
        data = {
            'auth_token': request.cookies.get('app_session'),
        }
        return response_message(200, 'success', 'Successfully get session data.', data)

    @middleware
    def post(self, auth):
        return self.get(auth)