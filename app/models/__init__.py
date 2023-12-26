"""
This file contains the models for the database. Models are classes that represent tables in the database.
We use SQLAlchemy to define our models. SQLAlchemy is an ORM (Object Relational Mapper) that allows us to
interact with the database using Python objects instead of SQL queries. This makes it easier to work with
the database and allows us to use the same code to interact with different database engines (e.g SQLite, MySQL, PostgreSQL).
Refer to this : https://docs.sqlalchemy.org/en/20/ for quickstarts and more information on SQLAlchemy.
"""

from sqlalchemy import Unicode

from app.models.extensions import db  # the db object is defined in extensions.py

# class Event(db.Model):
#     ...


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(Unicode(255), unique=True)
    hashed_password = db.Column(db.String(255))

    def __repr__(self):
        return f"<User(first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"
