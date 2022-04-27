import os

from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

from config import DevelopmentConfig, TestingConfig, ProductionConfig

load_dotenv()
app = Flask(__name__)
CORS(app)

if os.getenv('ENV').lower() == 'development':
    app_settings = DevelopmentConfig
    app.config.from_object(app_settings)
elif os.getenv('ENV').lower() == 'testing':
    app_settings = TestingConfig
    app.config.from_object(app_settings)
elif os.getenv('ENV').lower() == 'production':
    app_settings = ProductionConfig
    app.config.from_object(app_settings)
else:
    app_settings = DevelopmentConfig
    app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

