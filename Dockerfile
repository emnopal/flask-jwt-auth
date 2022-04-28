FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/flaskapp/src
COPY ./requirements.txt /opt/services/flaskapp/src
WORKDIR /opt/services/flaskapp/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /opt/services/flaskapp/src

EXPOSE 5090

CMD gunicorn --worker-class gevent --workers 8 --bind ${APP_HOST}:${APP_PORT} wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
