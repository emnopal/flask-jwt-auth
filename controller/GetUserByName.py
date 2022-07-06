from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from flask_restful import Resource
from helper import response_message, Serializers, RequestResponse, RequestPost
from model import User
from middleware import TokenRequired


class GetUserByName(MethodResource):
    fields = RequestResponse.fields_

    @doc(
        description='Get User by Name',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs(
        {
            'name': fields.Str(),
            'username': fields.Str(),
            'mail': fields.Str(),
            'page_size': fields.Int(),
            'page': fields.Int(),
        },
        location="query"
    )
    @marshal_with(RequestResponse)
    @TokenRequired
    def get(self, auth, **kwargs):

        args = request.args
        data = []

        by_name = args.get('name')
        by_username = args.get('username')
        by_mail = args.get('mail')

        args_for_filtering = any([by_name, by_username, by_mail])

        # Get user based by name or mail or username
        if args_for_filtering:

            if by_name:
                result = User.query.filter(User.name.contains(by_name)).all()
            if by_username:
                result = User.query.filter(User.username.contains(by_username)).all()
            if by_mail:
                result = User.query.filter(User.email.contains(by_mail)).all()

            for num, user in enumerate(result):
                data.append(Serializers(user).SerializeUserData(num))

        # Return all user
        else:
            users = User.query.all()
            for num, user in enumerate(users):
                data.append(Serializers(user).SerializeUserData(num))

        # Paginating the data
        page_size = args.get('page_size') if args.get('page_size') else None
        page = args.get('page') if args.get('page') else None

        paginate_results = Serializers(data).PaginateData(page_size, page)

        return response_message(200, 'success', 'Successfully get user data.', paginate_results)
