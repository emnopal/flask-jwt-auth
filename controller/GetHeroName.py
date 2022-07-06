import requests
from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from helper import response_message, RequestResponse
from middleware import TokenRequired


class GetHeroName(MethodResource):
    fields = RequestResponse.fields_

    @doc(
        description='Get Hero Name',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @use_kwargs({'q': fields.Str()}, location="query")
    @marshal_with(RequestResponse)
    @TokenRequired
    def get(self, auth, **kwargs):
        args = request.args
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
