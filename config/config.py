import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DATABASE')
database_test = os.getenv('DATABASE')
# database_test = os.getenv('DATABASE_TEST')

postgres_local_base = f'postgresql://{username}:{password}@{host}:{port}/'

cookie_name = "app_session"


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    # SQLALCHEMY_DATABASE_URI = postgres_local_base + database
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_test


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_test
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'other_prod_secret_key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
