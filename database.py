import datetime
import uuid
import peewee
import env

db = peewee.PostgresqlDatabase(env.DATABASE_NAME, user = env.DATABASE_USER_NAME, password = env.DATABASE_PASSWORD, host = env.DATABASE_HOST, port = env.DATABASE_PORT)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Users(BaseModel):
    id = peewee.UUIDField(unique=True, default=uuid.uuid4())
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    country_code = peewee.SmallIntegerField(null=True, default=91)
    mobile_number = peewee.BigIntegerField(unique=True, null=True)
    password_hash = peewee.CharField()
    created_at = peewee.DateField(default=datetime.datetime.now())
    updated_at = peewee.DateField(default=datetime.datetime.now())

class Transactions(BaseModel):
    id = peewee.UUIDField(unique=True, default=uuid.uuid4())
    event = peewee.SmallIntegerField()
    category = peewee.CharField()
    description = peewee.CharField(null=True)
    amount = peewee.FloatField()
    currency = peewee.CharField()
    date = peewee.DateField(default=datetime.datetime.now())
    created_at = peewee.DateField(default=datetime.datetime.now())
    updated_at = peewee.DateField(default=datetime.datetime.now())
