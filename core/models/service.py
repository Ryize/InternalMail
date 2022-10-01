import uuid

from core.models.base import SessionLocal


class _DB:
    db = SessionLocal()


def get_db():
    db = _DB().db
    try:
        return db
    finally:
        db.close()


def get_auth_code():
    return str(uuid.uuid4()).replace("-", "")
