import re
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from config import db


class BaseModel(db.Model):
    __abstract__ = True  # this is a base class, not a table

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    @declared_attr
    def __tablename__(cls):
        """Generates table name automatically based on the class name."""

        # convert table name to snake casing
        cls_name = cls.__name__
        tablename = re.sub(r"(?<!^)(?=[A-Z])", "_", cls_name)

        return tablename.lower()
