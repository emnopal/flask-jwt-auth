from flask_apispec import MethodResource, use_kwargs, marshal_with, doc
from helper import response_message, RequestResponse, RequestPost
from middleware import TokenRequired
from model import User
from controller import db, bcrypt


class UpdateUserInformationRequestPost(RequestPost):
    fields_ = RequestPost.fields_
    name = fields_.Str(required=True, description="Input Field for Name, this is required")
    email = fields_.Str(required=True, description="Input Field for Email, this is required and must be unique")
    username = fields_.Str(required=True, description="Input Field for Username, this is required and must be unique")
    password = fields_.Str(required=True, description="Input Field for Password, this is required")


class UpdateUserInformation(MethodResource):

    @doc(
        description='Update User Information',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(UpdateUserInformationRequestPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def patch(self, auth, **kwargs):
        try:
            user = User.query.filter_by(username=str(kwargs.get('username'))).first()
            if user and user.username == auth['resp']['sub']['username']:
                if bcrypt.check_password_hash(user.password, str(kwargs.get('password'))):
                    try:
                        user.name = str(kwargs.get('name'))
                        user.email = str(kwargs.get('email'))
                        db.session.commit()
                        return response_message(200, 'success', 'Successfully updated data.')
                    except:
                        return response_message(500, 'fail', 'Email already exists.')
                else:
                    return response_message(401, 'fail', 'You have no permission to update data.')
            else:
                return response_message(404, 'fail', "User doesn't exist.")
        except Exception as e:
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')
