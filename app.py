# pylint: disable=missing-module-docstring

import os
import secrets
import argparse
import dotenv
from docs import app
from model import db

parser = argparse.ArgumentParser()
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

parser.add_argument('-c', '--command', help='Command for tweaking flask app', type=str)
parser.add_argument('-s', '--set-staging', help='Set Default Staging', type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    HOST = app.config.get('APP_HOST')
    PORT = app.config.get('APP_PORT')
    DEBUG = app.config.get('DEBUG')

    if args.command:
        if args.command.lower() == 'migrate':
            db.create_all()
        elif args.command.lower() == 'refresh':
            os.environ["SECRET_KEY"] = secrets.token_urlsafe(64)
            dotenv.set_key(dotenv_file, "SECRET_KEY", os.environ["SECRET_KEY"], quote_mode='never')

        else:
            parser.error('unknown command.')

    if args.set_staging:
        if args.set_staging.lower() in ['development', 'testing', 'production']:
            os.environ["APP_ENV"] = args.set_staging.lower()
            dotenv.set_key(dotenv_file, "APP_ENV", os.environ["APP_ENV"], quote_mode='never')
        else:
            parser.error('unknown staging status.')

    else:
        app.run(host=HOST, port=PORT, debug=DEBUG)
