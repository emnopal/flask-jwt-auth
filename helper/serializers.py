import math
import re
from typing import TypeVar, Union
from model import User

T = TypeVar("T")
Num = TypeVar("Num", int, str)
PaginationNum = TypeVar("PaginationNum", int, str, None)


class Serializers:

    def __init__(self, data: T) -> None:
        self.data: T = data
        self.data_dict: dict[T, T] = {}
        self.data_list: list[T] = []

    def SerializeUserData(self, num: Num) -> dict[T, T]:
        self.data_dict[f'user_{num}'] = {
            'username': self.data.username,
            'name': self.data.name,
            'email': self.data.email,
            'registered_on': self.data.registered_on,
            'status': 'online' if self.data.last_logged_in else 'offline',
            'last_online': self.data.last_logged_out if self.data.last_logged_in and self.data.last_logged_out
            else 'now' if self.data.last_logged_in else 'never',
            'last_logged_in': self.data.last_logged_in,
            'last_logged_out': self.data.last_logged_out,
        }
        return self.data_dict

    def PaginateData(self, page_size: PaginationNum, page: PaginationNum) -> dict[T, T]:

        page_size = 10 if not page_size else page_size
        page = 1 if not page else page

        prev_page = None
        next_page = None
        total_page_number = 1
        current_page = 1

        page_size = int(page_size)
        count = len(self.data)
        total_page_number = math.ceil(count / page_size)

        if page:
            current_page = int(page)
        else:
            current_page = 1  # Default page Number

        start = page_size * (current_page - 1)
        stop = current_page * page_size
        paginate_data = self.data[start:stop]
        next_page = current_page + 1 if 0 < current_page + 1 <= total_page_number else None
        prev_page = current_page - 1 if 0 < current_page - 1 <= total_page_number else None

        return {
            "prev": prev_page,
            "current": current_page,
            "next": next_page,
            "total_pages": total_page_number,
            'length_data': len(self.data),
            'length_paginate_data': len(paginate_data),
            'data': paginate_data,
        }

    @staticmethod
    def CheckMail(mail: str) -> Union[str, ValueError]:

        email = str(mail)  # make sure the data is string
        is_valid = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(is_valid, email):
            return email
        else:
            raise ValueError("Invalid email")

    def ValidatingRegister(self) -> Union[User, TypeError]:

        if isinstance(self.data, dict):
            sorted_json_requests = sorted(self.data.keys())
            required_json_requests = sorted(['username', 'password', 'email', 'name'])

            if sorted_json_requests != required_json_requests:
                message = f"Please Provide: {', '.join(list(set(required_json_requests).difference(sorted_json_requests)))}"
                raise ValueError(message)

            return User(
                username=str(self.data.get('username')),
                password=str(self.data.get('password')),
                email=self.CheckMail(self.data.get('email')),
                name=str(self.data.get('name'))
            )

        raise TypeError("Not a valid json")
