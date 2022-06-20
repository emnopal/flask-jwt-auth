from model import User
from helper import check_mail

def validate_register(data):
    sorted_json_requests = sorted(data.keys())
    required_json_requests = sorted(['username', 'password', 'email', 'name'])

    if sorted_json_requests != required_json_requests:
        message = f"Please Provide: {', '.join(list(set(required_json_requests).difference(sorted_json_requests)))}"
        raise ValueError(message)

    return User(
        username=str(data.get('username')),
        password=str(data.get('password')),
        email=check_mail(data.get('email')),
        name=str(data.get('name'))
    )
