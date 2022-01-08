FROM python:3.9.7

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/app/

RUN python migrate.py

CMD ["python", "app.py"]