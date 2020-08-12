import os
from app import create_app
from models.models import User
app = create_app(os.getenv("APP_SETTINGS") or "default")


# add admin to the db
@app.cli.command()
def create_admin():
    """create an administrator"""
    user = User(username='nick', email='yegonicholas@gmail.com', password='SkodoSuperb1', is_admin=True)
    user.add()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """run flask application in debug mode."""
    app.run()
