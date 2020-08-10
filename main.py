import os
import click

from app import create_app
app = create_app(os.getenv("APP_SETTINGS") or "default")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """run flask application in debug mode."""
    app.run(debug=True)
