import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# load env vars
load_dotenv()


BASE_DIR = Path(__file__).parent.parent


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


class Base(DeclarativeBase):
    pass


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    # CKEDITOR_PKG_TYPE = "standard"


db = SQLAlchemy(model_class=Base)
ckeditor = CKEditor()


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    ckeditor.init_app(app)

    login_manager.init_app(app)
    mail.init_app(app)

    from app.errors.handlers import errors
    from app.main.routes import main
    from app.posts.routes import posts
    from app.users.routes import users

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    with app.app_context():
        db.create_all()

    return app
