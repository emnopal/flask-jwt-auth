# Flask JWT Authentication

## Description

Implementation of JWT (JSON Web Token) authentication for: <br>

    - Register User
    - Login User
    - Logout User
    - Refresh Token
    - Revoke Token
    - Get User Info
    - Get All Users info in Database by name
    - Update User Info (Username, Password, Email, and Name)
    - Referral Code Validation
    - Referral Code Generation
    - Get Authenticated Data

Using Python with Flask as backend framework to create REST API and
PostgreSQL as database with SQLAlchemy as SQL Connector to Python.

## Usage

### Using localhost

- Create new python venv: `python -m venv <venv_name>`
- Activate python venv: `source <venv_name>/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Migrate database: `python migrate.py`
- Run development server: `python app.py`
- Access API in `http://localhost:5090`

### Using docker

- Generate your own .env files in `/` with parameter:
  - DB_USERNAME as Postgres Username
  - DB_PASSWORD as Postgres Password
  - DB_PORT as Postgres Port
  - DB_HOST as Postgres Host
  - DATABASE as Postgres Database Name
  - DATABASE_TEST as Postgres Database (For Development) Name
  - SECRET_KEY as Generate your own secret_key for JWT
- Run docker compose:<br>
    `$ docker-compose up -d db && docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python migrate.py" && docker-compose up -d`
- Access API in:<br>
   `http://localhost:8080`

For API testing, I suggest you to use [Postman](https://www.postman.com/) for testing the API. <br><br>


## API Documentation

For API Docs, you can use Swagger to view the docs. <br>

- You can access it (Swagger UI) through: `http://localhost:5090/docs` <br>
- or you can generate json from: `http://localhost:5090/docs/json` <br>
Note: Change it to 8080 if you are using docker.<br>


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
