import jwt
import datetime

from typing import TypeVar, Optional, Union
from model import BlacklistToken

from src import app

T = TypeVar("T")


class Auth:

    def __init__(self, token: Optional[str] = None, data: Union[dict[T, T], str, None] = None) -> None:
        self.token: Optional[str] = token
        self.data: Union[dict[T, T], str] = data
        self.conf = app.config

    @staticmethod
    def CheckBlacklist(token: str) -> bool:
        res = BlacklistToken.query.filter_by(token=str(token)).first()
        return bool(res)

    def DecodeAuthToken(self) -> Union[str, dict[T, T]]:
        try:
            payload = jwt.decode(self.token, self.conf.get('SECRET_KEY'), algorithms='HS256')
            is_blacklisted_token = self.CheckBlacklist(self.token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError as e:
            return f'Invalid token. Please log in again. {e}'

    def EncodeAuthToken(self) -> Union[str, Exception]:
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=int(self.conf.get('TOKEN_EXPIRED'))),
                'iat': datetime.datetime.utcnow(),
                'sub': {
                    'data': self.data
                }
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
