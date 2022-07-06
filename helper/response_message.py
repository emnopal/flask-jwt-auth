from typing import Union, Optional, TypeVar
from flask import jsonify, make_response, request
from flask.wrappers import Response

T = TypeVar("T")


def response_message(status_code: Union[str, int], status: str, message: str = "",
                     data: Union[str, dict[T, T], None] = None) -> Response:
    if data is None:
        return make_response(
            jsonify({
                'status': status,
                'message': message,
                'status_code': status_code,
                'method': request.method
            }),
            status_code
        )
    else:
        return make_response(
            jsonify({
                'status': status,
                'message': message,
                'status_code': status_code,
                'method': request.method,
                'data': data
            }),
            status_code
        )
