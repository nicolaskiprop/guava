# imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
import datetime
from werkzeug.security import check_password_hash

# local imports
from Utils import validators
from models.models import User


class SignUp(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username", type=str, required=True, help="this field cannot be blank")

    parser.add_argument("email", type=str, required=True, help="this field cannot be blank")

    parser.add_argument("password", type=str, required=True, help="this field cannot be blank")

    def post(self):
        """create new user"""
        data = SignUp.parser.parse_arg()
        username = data["username"]
        email = data["email"]
        password = data["password"]

        validate = validators.Validators()

        """validate user data before submission"""

        if not validate.valid_name("username"):
            return {"status": 400, "message": "please provide a valid username"}, 400
        if not validate.valid_email("email"):
            return {"status": 400, "message": "please provide a valid email"}, 400
        if not validate.valid_password("password"):
            return {"status": 400, "message": "password should start with a capital letter, "
                                              "include a number and should be not less than 8 characters long"}, 400
        if User().fetch_by_username(username):
            return {"status": 400, "message": "user already exist"}, 400
        user = User(username, email, password)

        user_exist = User().get_user_by_email(email)
        if user_exist:
            return {"status": 400, "message": "This user already exists"}, 400
        User.add()
        expires = datetime.timedelta(minutes=60)
        token = create_access_token(identity=user.serialize(), expires_delta=expires)

        user_exist = User().get_user_by_email(email)

        return {
            "message": "Account created successfully",
            "access_token": token,
            "user": user_exist.serialize()
        }


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="provide email")
    parser.add_argument("password", type=str, required=True, help="This field cannot be empty")

    def post(self):
        """login user"""
        login_data = Login.parser.parse_arg()

        username = login_data["username"]
        password = login_data["password"]

        validate = validators.Validators()

        user = User().fetch_by_username(username)

        if not user:
            return {
                       "status": 404,
                       "message": "user not found"
                   }, 404

        if not check_password_hash(user.password_hash, password):
            return {"status": 401, "message": 'incorrect password'}, 401
        expires = datetime.timedelta(minutes=30)
        token = create_access_token(
            identity=user.serialize(), expires_delta=expires)
        return {
                   'status': 200,
                   'token': token,
                   'message': 'successfully logged in'
               }, 200
