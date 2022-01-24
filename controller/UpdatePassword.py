import requests
from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from helper.message import response_message
from model import User, BlacklistToken
from controller import db, bcrypt, app
from helper.decode_auth_token import decode_auth_token


class UpdatePassword(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
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
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                try:
                    user = User.query.filter_by(username=post_data.get('username')).first()
                    if user and user.username == resp['sub']['username']:
                        if bcrypt.check_password_hash(user.password, post_data.get('old_password')):
                            try:
                                user.password = bcrypt.generate_password_hash(
                                    post_data.get('new_password'), app.config.get('BCRYPT_LOG_ROUNDS')
                                ).decode('utf-8')
                                db.session.commit()
                                return response_message(200, 'success', 'Successfully changed password.')
                            except:
                                return response_message(500, 'fail', 'Failed changed password.')
                        else:
                            return response_message(401, 'fail', 'You have no permission to update data.')
                    else:
                        return response_message(404, 'fail', "User doesn't exist.")
                except Exception as e:
                    return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')
        return response_message(401, 'fail', 'Session does not exists or not a valid token, Please login.')

    def put(self):
        return self.post()

    def patch(self):
        return self.post()


class UpdateUsername(MethodResource, Resource):
    def post(self):
        post_data = request.get_json()
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
                try:
                    user = User.query.filter_by(username=post_data.get('old_username')).first()
                    if user and user.username == resp['sub']['username']:
                        if bcrypt.check_password_hash(user.password, post_data.get('password')):
                            try:
                                user.username = post_data.get('new_username')
                                db.session.commit()
                                new_user = User.query.filter_by(username=post_data.get('new_username')).first()
                                if new_user:
                                    new_auth_token = new_user.encode_auth_token(new_user.username)
                                    data = {
                                        'new_auth_token': new_auth_token
                                    }
                                    res = response_message(200, 'success', 'Successfully changed username.', data)
                                    res.set_cookie('app_session', new_auth_token, max_age=60 * 60)
                                    return res
                                else:
                                    raise Exception
                            except:
                                return response_message(500, 'fail', 'Failed changed username.')
                        else:
                            return response_message(401, 'fail', 'You have no permission to update data.')
                    else:
                        return response_message(404, 'fail', "User doesn't exist.")
                except Exception as e:
                    return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')
        return response_message(401, 'fail', 'Session does not exists or not a valid token, Please login.')

    def put(self):
        return self.post()

    def patch(self):
        return self.post()


class UserAPI(MethodResource, Resource):
    def get(self):
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
                user = User.query.filter_by(username=resp['sub']['username']).first()
                data = {
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


class GetReferralCode(MethodResource, Resource):
    def get(self):
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
                user = User.query.filter_by(username=resp['sub']['username']).first()
                data = {
                    'referral_code': user.referral_code,
                }
                return response_message(200, 'success', 'Successfully get referral code.', data)
            return response_message(401, 'fail', resp)
        else:
            return response_message(401, 'fail', 'Provide a valid auth token.')

    def post(self):
        return self.get()


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
            resp = User.decode_auth_token(auth_token)
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
