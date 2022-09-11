
from datetime import timedelta
from wtforms import SubmitField
from flask_wtf.file import FileField
from flask_wtf import FlaskForm
from flask_login import LoginManager
from os import path
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentCofig")

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

    app.app_context().push()

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .myforms import DlyProduction

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# def create_database(app):
#    if not path.exists('website/'+DB_NAME):
#        db.create_all(app=app)
#        print('Created Database!')
