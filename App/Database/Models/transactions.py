import peewee
import Database.Models.base_model
import pydantic
import typing
import uuid
import datetime

class Transactions(Database.Models.base_model.BaseModel):
    id = peewee.UUIDField(unique=True)
    user_id = peewee.UUIDField()
    event = peewee.SmallIntegerField()
    category = peewee.CharField()
    description = peewee.CharField(null=True)
    amount = peewee.FloatField()
    currency = peewee.CharField()
    date = peewee.DateField()
    status = peewee.SmallIntegerField()
    created_at = peewee.DateField()
    updated_at = peewee.DateField()

class TransactionModel(pydantic.BaseModel):
    user_id : uuid.UUID
    event: int
    category: str
    description: typing.Optional[str] = None
    amount: int
    currency: str
    date: typing.Optional[datetime.datetime] = None
