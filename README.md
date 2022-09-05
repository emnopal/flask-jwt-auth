# Flask JWT Authentication

## Description

Implementation of JWT (JSON Web Token) authentication using Python <br>
with Flask as backend framework to create REST API and PostgreSQL <br>
as database with SQLAlchemy as SQL Connector to Python.

## Usage

### Using localhost

- Create new python venv: `python -m venv <venv_name>`
- Activate python venv: `source <venv_name>/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Migrate database: `python app.py -c migrate`
- Run development server: `python app.py`

### Using docker

- Just Run docker compose:<br>
    `$ docker-compose up -d db && docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python app.py -c migrate" && docker-compose up -d`
- CAUTION: Fix This!

For API testing, I suggest you to use [Postman](https://www.postman.com/) for testing the API. <br><br>

## API Documentation

For API Docs, you can use Swagger to view the docs. <br>

- You can access it (Swagger UI) through: `<path_to_API>/docs` <br>
- or you can generate json from: `<path_to_API>/docs/json` <br>


## To Do

- Unit Testing
- Logger
- Fix Routing [Done]
- Add Redis
- Add Async

Please refer to this:

- https://github.com/cirobarradov/flask-redis
- https://github.com/popescuaaa/glowing-palm-tree
- https://github.com/chiragchamoli/flask-restful-api-boilerplate
- https://github.com/jwalin12/cacheAPI
- https://github.com/nahid111/flask-app
- https://github.com/tomimick/restpie3
