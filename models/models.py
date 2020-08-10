# imports
from datetime import datetime
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from flask import current_app


class Datastore:
    """database connection model"""

    def __init__(self):
        self.db_host = current_app.config['DB_HOST']
        self.db_username = current_app['DB_USERNAME']
        self.db_password = current_app['DB_PASSWORD']
        self.db_name = current_app['DB_NAME']

        # connect to db
        self.conn = psycopg2.connect(
            host=self.db_host,
            user=self.db_username,
            password=self.db_password,
            database=self.db_name,
        )
        # open cursor to perform db ops
        self.cur - self.conn.cursor()

    def create_table(self, schema):
        """method to create table"""
        self.cur.execute(schema)
        self.save()

    def drop_table(self, name):
        """method to drop a table"""
        self.cur.execute("DROP TABLE IF EXISTS" + name)
        self.save()

    def save(self):
        """method to save changes"""
        self.conn.commit()

    def close(self):
        self.cur.close()


class User(Datastore):

    def __init__(self, username=None, email=None, password=None, is_admin=False):
        super().__init__()
        self.username = username
        self.email = email
        if password:
            self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    def create(self):
        """create table users"""
        self.create_table("""
         Create Table Users(
            id serial PRIMARY KEY
            username VARCHAR NOT NULL
            email VARCHAR NOT NULL
            password VARCHAR NOT NULL
            is_admin BOOLEAN NOT NULL
         );
         """
                          )
