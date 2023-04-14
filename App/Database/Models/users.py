import peewee
import Database.Models.base_model
import pydantic
import typing
import playhouse.postgres_ext


class Users(Database.Models.base_model.BaseModel):
    id = peewee.UUIDField(unique=True)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    country_code = peewee.SmallIntegerField(null=True)
    mobile_number = peewee.BigIntegerField(null=True)
    password = peewee.CharField()
    user_session = playhouse.postgres_ext.BinaryJSONField()
    status = peewee.SmallIntegerField()
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField()


class UserModel(pydantic.BaseModel):
    name: str
    email: str
    country_code: typing.Optional[int] = None
    mobile_number: typing.Optional[int] = None
    password: str
    user_session: typing.Optional[dict] = {}
