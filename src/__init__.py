from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import DevelopmentConfig, TestingConfig

app = Flask(__name__)
CORS(app)

app_settings = DevelopmentConfig
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

