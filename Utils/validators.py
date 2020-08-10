# module import
import re


class Validators:
    def valid_name(self, username):
        """valid username"""
        return re.match("^[a-zA-Z]+$", username)

    def valid_password(self, password):
        """validate password"""
        return re.match(password, "^(?=.*[A-Z])(?=.*[a-z](?=.*[0-9)[a-zA-Z0-9]{8,15}$")

    def valid_email(self, email):
        """validate email"""
        return re.match("^[^@]+@[^@]+\.[^@]+$", email)

    def valid_inputs(self, string_inputs):
        """validate inputs"""
        return re.match("^[a-zA-Z0-9-._@ ']+$", string_inputs)

