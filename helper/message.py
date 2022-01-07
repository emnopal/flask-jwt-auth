from flask import jsonify, make_response, request


def response_message(status_code, status, message="", data=None):
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
