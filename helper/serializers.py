import math

class Serializers:

    def __init__(self, data):
        self.data = data
        self.data_dict = {}
        self.data_list = []

    def SerializeUserData(self, num):
        self.data_dict[f'user_{num}'] = {
            'username': self.data.username,
            'name': self.data.name,
            'email': self.data.email,
            'registered_on': self.data.registered_on,
            'status': 'online' if self.data.last_logged_in else 'offline',
            'last_online': self.data.last_logged_out if self.data.last_logged_in and self.data.last_logged_out\
                else 'now' if self.data.last_logged_in else 'never',
            'last_logged_in': self.data.last_logged_in,
            'last_logged_out': self.data.last_logged_out,
        }
        return self.data_dict

    def PaginateData(self, page_size, page):

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

        paginate_results = {
            "prev": prev_page,
            "current": current_page,
            "next": next_page,
            "total_pages": total_page_number,
            'length_data': len(self.data),
            'length_paginate_data': len(paginate_data),
            'data': paginate_data,
        }

        return paginate_results
