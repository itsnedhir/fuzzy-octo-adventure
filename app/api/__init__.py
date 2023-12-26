from pathlib import Path

from flask import Flask

from app.api.user import bp as user_bp
from app.models.extensions import db

# Get the parent of the parent of this file using Pathlib


ROOT_DIR = Path(__file__).parent.parent
DB_PATH = (ROOT_DIR / "db" / "db.sqlite3").as_posix()


def create_app(database_uri: str = f"sqlite:///{DB_PATH}") -> Flask:
    """
    Creates the Flask app and initializes the database.
    :param database_uri: The database URI to connect to.
        This parameter is useful if we decide to use another db service
        or a db service on the cloud (e.g AWS RDS) we could simply read this from
        the config or environment variables.
    :return: The Flask app.
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(user_bp)

    return app
