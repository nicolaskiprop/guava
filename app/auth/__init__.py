from flask import Blueprint
from .auth import SignUp

auth_blueprint = Blueprint("auth", __name__)

