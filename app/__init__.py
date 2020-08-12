# imports
from flask import Flask, redirect, url_for
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# local imports
from Instance.config import app_config
from .auth.auth import SignUp, Login

jwt = JWTManager()


# application factory

def create_app(config_mode):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app.config)
    app.config.from_pyfile('config.py', silent=True)

    jwt.init_app(app)
    CORS(app)

    @app.route('/')
    def index():
        return redirect('https://nickdee.docs.apiary.io')

    # registering blueprints for my views

    from .admin import admin_blueprint as admin_blp

    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix="/api/v2")

    from .auth import auth_blueprint as auth_blp

    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix="/api/v2")

    # Routes
    auth.add_resource(SignUp, '/auth/signup')
    auth.add_resource(Login, '/auth/Login')

    return app
