from model import db


def migrate():
    db.create_all()


if __name__ == '__main__':
    migrate()