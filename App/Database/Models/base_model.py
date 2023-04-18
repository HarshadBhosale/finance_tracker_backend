from peewee import Model
from Database.database import database


class BaseModel(Model):
    class Meta:
        database = database
