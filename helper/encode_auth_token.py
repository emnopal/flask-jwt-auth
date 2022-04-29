import jwt
import datetime
from src import app

def encode_auth_token(username, expired):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expired),
            'iat': datetime.datetime.utcnow(),
            'sub': {
                'username': username
            }
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
