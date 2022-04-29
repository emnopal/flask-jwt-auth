import re

def check_mail(email):
    is_valid = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(is_valid, email)):
        return email
    else:
        raise ValueError("Invalid mail")
