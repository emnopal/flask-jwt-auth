import argparse
import sys
from docs import app
from model import db

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--command', default=False, help='Migrating database')

if __name__ == '__main__':
    args = parser.parse_args()

    HOST = app.config.get('APP_HOST')
    PORT = app.config.get('APP_PORT')
    DEBUG = app.config.get('DEBUG')

    if args.command == 'migrate':
        db.create_all()
        sys.exit()
    else:
        app.run(host=HOST, port=PORT, debug=DEBUG)
