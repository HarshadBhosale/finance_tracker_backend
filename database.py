import peewee
import env

db = peewee.PostgresqlDatabase(env.DATABASE_NAME, autorollback = True, user = env.DATABASE_USER_NAME, password = env.DATABASE_PASSWORD, host = env.DATABASE_HOST, port = env.DATABASE_PORT)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Users(BaseModel):
    id = peewee.UUIDField(unique=True)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    country_code = peewee.SmallIntegerField(null=True)
    mobile_number = peewee.BigIntegerField(null=True)
    password_hash = peewee.CharField()
    status = peewee.SmallIntegerField()
    created_at = peewee.DateField()
    updated_at = peewee.DateField()

class Transactions(BaseModel):
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
