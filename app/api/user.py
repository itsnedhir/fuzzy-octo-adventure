import logging
from typing import Optional

from flask import Blueprint

from app.models import User
from app.models.extensions import db

logger = logging.getLogger(__name__)

# Define User Blueprint : all endpoints with prefix /user
bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Gets a user by id.
    :param user_id: The user id.
    :return: The user if found, else None.
    """
    # Query database for user by id and return the result if found else return None

    return f"<User: {user_id}>"
