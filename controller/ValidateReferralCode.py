import requests
from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User, BlacklistToken
from controller import db
from helper.decode_auth_token import decode_auth_token


class ValidateReferralCode(MethodResource, Resource):
    def post(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        post_data = request.get_json()
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(username=resp['sub']['username']).first()
                if user.referral_code != post_data['referral_code']:
                    if User.query.filter_by(referral_code=post_data['referral_code']).first():
                        return response_message(200, 'success', 'Valid referral code.')
                return response_message(401, 'fail', 'Invalid referral code.')
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def get(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        args = request.args
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(username=resp['sub']['username']).first()
                if user.referral_code != args.get('ref'):
                    if User.query.filter_by(referral_code=args.get('ref')).first():
                        return response_message(200, 'success', 'Valid referral code.')
                return response_message(401, 'fail', 'Invalid referral code.')
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')


class FindByName(MethodResource, Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        args = request.args
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                data = {}
                if args:
                    users = User.query.filter(User.name.contains(args.get('name'))).all()
                    for num, user in enumerate(users):
                        data[f'user_{num}'] = {
                            'username': user.username,
                            'name': user.name,
                            'email': user.email,
                            'referral_code': user.referral_code,
                            'registered_on': user.registered_on
                        }
                    return response_message(200, 'success', 'Successfully get user data.', data)
                users = User.query.all()
                for num, user in enumerate(users):
                    data[f'user_{num}'] = {
                        'username': user.username,
                        'name': user.name,
                        'email': user.email,
                        'referral_code': user.referral_code,
                        'registered_on': user.registered_on
                    }
                return response_message(200, 'success', 'Successfully get user data.', data)
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()


class GetHeroName(MethodResource, Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        args = request.args
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                data = {}
                r = requests.get('https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
                if args:
                    for key, value in r.json()['data'].items():
                        if args.get('q').title() in key:
                            data[key] = value
                    return response_message(200, 'success', 'Successfully get hero data.', data)
                for key, value in r.json()['data'].items():
                    data[key] = value
                return response_message(200, 'success', 'Successfully get hero data.', data)
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()


class LogoutAPI(MethodResource, Resource):
    def post(self):
        auth_header = request.headers.get('Authorization')
        auth_cookie = request.cookies.get('app_session')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_message(401, 'fail', 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token and auth_cookie and auth_token == auth_cookie:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    db.session.add(blacklist_token)
                    db.session.commit()
                    res = response_message(200, 'success', 'Successfully logged out.')
                    res.set_cookie('app_session', '', expires=0)
                    return res
                except Exception as e:
                    return response_message(500, 'fail', f'Internal Server Error, with error: {e}.')
            else:
                return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def get(self):
        return self.post()

    def delete(self):
        return self.post()
