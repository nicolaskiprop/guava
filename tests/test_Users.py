import unittest
import json

from .base_test import BaseTest


class TestUser(BaseTest):

    def test_signup(self):
        """test for signup successful"""
        response = self.signup()
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        """test for login successful"""
        self.signup()
        response = self.login()

        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_as_admin(self):
        """test to login admin"""
        response = self.login_admin()
        self.assertEqual(response.status_code, 200)

    def test_incorrect_password(self):
        """test for incorrect password"""
        self.signup()
        response = self.client.post(
            "api/auth/login",
            data=json.dumps(self.incorrects_pass_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 401)

    def test_email_exists(self):
        """test signup with an existing email"""
        self.signup()
        response = self.client.post(
            "api/auth/signup",
            data=json.dumps(self.email_already_exists_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

    def test_existing_username(self):
        """Test signup with existing username"""
        self.signup()
        response = self.client.post(
            "api/auth/signup",
            data=json.dumps(self.existing_username_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

    def test_non_existing_user_login(self):
        """test when user don't exist"""
        self.signup()
        response = self.client.post(
            "api/auth/login",
            data=json.dumps(self.user_doesnt_exist_data),
            headers={'content-type': 'application/json'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)["message"], "user not found")

    def test_invalid_username(self):
        """Test if username is invalid"""
        response = self.client.post(
            "api/auth/signup",
            data=json.dump(self.invalid_username_data),
            headers={'content-type': 'application.json'}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        """tests if email is invalid"""
        response = self.client.post(
            "api/auth/signup",
            data=json.dumps(self.invalid_email_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "enter a valid email ")

    def test_invalid_password(self):
        """tests invalid password"""
        response = self.client.post(
            "api/auth/signup",
            data=json.dumps(self.invalid_password_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
