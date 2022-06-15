from model import User
from helper import check_mail

def validate_register(data):
    if data.keys() != ['username', 'password', 'email', 'name']:
        message = f"Please Provide: {', '.join(list(set(['username', 'password', 'email', 'name']).difference(data.keys())))}"
        raise ValueError(message)
    return User(
        username=str(data.get('username')),
        password=str(data.get('password')),
        email=check_mail(data.get('email')),
        name=str(data.get('name'))
    )
