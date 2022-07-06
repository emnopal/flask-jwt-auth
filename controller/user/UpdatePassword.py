from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse, RequestPost
from middleware import TokenRequired
from model import User
from controller import db, bcrypt, app


class UpdatePasswordRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    username = fields_.Str(required=True, description="Input Field for Name, this is required")
    old_password = fields_.Str(required=True, description="Input Field for Old Password, this is required")
    new_password = fields_.Str(required=True, description="Input Field for New Password, this is required")


class UpdatePassword(MethodResource):

    @doc(
        description='Update Password',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(UpdatePasswordRequestPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def patch(self, auth, **kwargs):
        try:
            user = User.query.filter_by(username=str(kwargs.get('username'))).first()
            if user and user.username == auth['resp']['sub']['data']['username']:
                if bcrypt.check_password_hash(user.password, kwargs.get('old_password')):
                    try:
                        user.password = bcrypt.generate_password_hash(
                            str(kwargs.get('new_password')), app.config.get('BCRYPT_LOG_ROUNDS')
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
