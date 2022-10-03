from core.models.service import get_db


class BaseMixin:
    db = get_db()

    def save(self):
        self.db.add(self)
        self.db.commit()

    @classmethod
    def create(cls, *args, **kwargs):
        object = cls(*args, **kwargs)
        cls.db.add(object)
        cls.db.commit()
