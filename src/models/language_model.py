from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, param: dict):
        super().__init__(param)

    # Req. 2
    def to_dict(self):
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    # Req. 3
    @classmethod
    def list_dicts(cls):
        result = []

        for language in cls._collection.find():
            result.append(
                {"name": language["name"], "acronym": language["acronym"]}
            )

        return result
