import unittest
import json

from app import create_app
from db_test import create_admin, drop, migrate


class BaseTest(unittest.TestCase):
    def setUp(self):
        """setting up testing"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            drop()
            migrate()
            create_admin()
        """insert here create data"""
        self.create_data = {}

        self.user_signup_data = {
            "username": "nick",
            "email": "yegonicholas@gmail.com",
            "password": "SkodoSuperb1"
        }
        self.user_login_data = {
            "username": "nick",
            "password": "SkodoSuperb1"
        }
        self.admin_login_data = {
            "username": "nickdee",
            "password": "undefeatedw1tness"
        }

    def signup(self):
        """user signup fxn"""
        response = self.client.post(
            "api/auth/signup",
            data=json.dumps(self.user_signup_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login(self):
        """login fxn"""
        response = self.client.post(
            "api/auth/login",
            data=json.dumps(self.user_login_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login_admin(self):
        """admin login fxn"""
        response = self.client.post(
            "api/auth/login",
            data=json.dumps(self.admin_login_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def get_token_as_user(self):
        """get user token"""
        self.signup()
        response = self.login()
        token = json.loads(response.data).get("token", None)
        return token

    def get_token_as_admin(self):
        """gets admin token"""
        response = self.login_admin()
        token = json.loads(response.data).get("token", None)
        return token
