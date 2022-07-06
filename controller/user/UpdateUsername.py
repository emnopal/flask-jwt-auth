from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from helper import response_message, Auth, RequestResponse, RequestPost
from middleware import TokenRequired
from model import User
from controller import db, bcrypt


class UpdateUsernameRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    old_username = fields_.Str(required=True, description="Input Field for Old Name, this is required")
    new_username = fields_.Str(required=True, description="Input Field for New Username, this is required")
    password = fields_.Str(required=True, description="Input Field for Password, this is required")


class UpdateUsername(MethodResource):

    @doc(
        description='Update Username',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(UpdateUsernameRequestPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def patch(self, auth, **kwargs):
        try:
            user = User.query.filter_by(username=str(kwargs.get('old_username'))).first()
            if user and user.username == auth['resp']['sub']['username']:
                if bcrypt.check_password_hash(user.password, str(kwargs.get('password'))):
                    try:
                        user.username = str(kwargs.get('new_username'))
                        db.session.commit()
                        new_user = User.query.filter_by(username=str(kwargs.get('new_username'))).first()
                        if new_user:
                            new_auth_token = Auth(data=str(new_user.username)).EncodeAuthToken()
                            data = {
                                'new_auth_token': new_auth_token
                            }
                            return response_message(200, 'success', 'Successfully changed username.', data)
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
