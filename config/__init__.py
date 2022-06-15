import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class BaseConfig:
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_NAME_TEST = os.getenv('DB_NAME_TEST')
    CONN = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/'

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_PORT = os.getenv('APP_PORT')
    APP_HOST = os.getenv('APP_HOST')
    APP_ENV = os.getenv('APP_ENV')
    APP_PREFIX = '/api'

    TOKEN_EXPIRED = 60*24*5


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = BaseConfig.CONN + BaseConfig.DB_NAME


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = BaseConfig.CONN + BaseConfig.DB_NAME_TEST
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = BaseConfig.CONN + BaseConfig.DB_NAME
