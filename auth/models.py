from flask_login.mixins import UserMixin

from config import db
from core.models import BaseModel


class User(UserMixin, BaseModel):
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    def __str__(self):
        return self.full_name
