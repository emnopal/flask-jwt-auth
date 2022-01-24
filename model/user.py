import uuid

import jwt
import datetime

from model import app, db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(255), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    referral_code = db.Column(db.String(255), nullable=False, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password, email, name):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode('utf-8')
        self.referral_code = uuid.uuid4()
        self.username = username
        self.name = name
        self.registered_on = datetime.datetime.now()

    def encode_auth_token(self, username):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
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
