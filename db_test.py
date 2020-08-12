import os
from models.models import User
from app import create_app

app = create_app('testing')


def migrate():
    """create table test"""
    User().create()


def drop():
    """drop table test"""
    User().drop()


def create_admin():
    """add admin"""
    user = User(username='nick', email='yegonicholas@gmail.com', password='SkodoSuperb1', is_admin=True)
    user().add()
