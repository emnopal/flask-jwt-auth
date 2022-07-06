import datetime
from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, Auth, RequestResponse, RequestPost
from model import User
from controller import bcrypt, db


class LoginRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    username = fields_.Str(required=True, description="Input Field for Username")
    password = fields_.Str(required=True, description="Input Field for Password")


class LoginAPI(MethodResource):

    @doc(
        description='Login Endpoint.',
    )
    @use_kwargs(LoginRequestPost, location='json')
    @marshal_with(RequestResponse)
    def post(self, **kwargs):
        try:
            user = User.query.filter_by(username=str(kwargs.get('username'))).first()
            if user and bcrypt.check_password_hash(str(user.password), str(kwargs.get('password'))):
                auth_token_data = {
                    'username': str(user.username)
                }
                auth_token = Auth(data=auth_token_data).EncodeAuthToken()
                if auth_token:
                    user.last_logged_in = datetime.datetime.now()
                    user.last_logged_out = None
                    db.session.commit()
                    data = {
                        'auth_token': auth_token,
                        'referral_code': user.referral_code
                    }
                    return response_message(200, 'success', 'Successfully logged in.', data)
            else:
                return response_message(404, 'fail', 'User does not exist or username or password not match.')
        except Exception as e:
            return response_message(401, 'fail', f'Username or password not match. {e}')
