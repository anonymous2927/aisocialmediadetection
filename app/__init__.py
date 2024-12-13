from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from app.config import Config  # Assuming Config class is in app/config.py

# Initialize extensions
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # Import routes after the app is created to avoid circular imports
    from app import routes

    return app
