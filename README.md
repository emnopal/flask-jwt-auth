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
- Create new python venv: `python -m venv <venv_name>`
- Activate python venv: `source <venv_name>/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run development server: `python app.py`

For API testing, I suggest you to use [Postman](https://www.postman.com/) for testing the API. <br><br>

## API Documentation
For API Docs, you can use Swagger to view the docs. <br>
- You can access it (Swagger UI) through: `http://localhost:5000/docs` <br>
- or you can generate json from: `http://localhost:5000/docs/json` <br>
    