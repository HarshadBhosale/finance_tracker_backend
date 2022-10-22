from peewee import PostgresqlDatabase, Model, CharField, DateField, UUIDField, SmallIntegerField, BigIntegerField, FloatField
from env import DATABASE_NAME, DATABASE_USER_NAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

db = PostgresqlDatabase(DATABASE_NAME, user = DATABASE_USER_NAME, password = DATABASE_PASSWORD, host = DATABASE_HOST, port = DATABASE_PORT)

class User(Model):
    id = UUIDField()
    name = CharField()
    email = CharField()
    country_code = SmallIntegerField()
    mobile_number = BigIntegerField()
    hashed_password = CharField()

    class Meta:
        database = db
        db_table = 'users'

class Expense(Model):
    id = UUIDField()
    category = CharField()
    description = CharField()
    amount = FloatField()
    currency = CharField()
    date = DateField()
    created_at = DateField()
    updated_at = DateField()

    class Meta:
        database = db
        db_table = 'expenses'

class Income(Model):
    id = UUIDField()
    category = CharField()
    description = CharField()
    amount = FloatField()
    currency = CharField()
    date = DateField()
    created_at = DateField()
    updated_at = DateField()

    class Meta:
        database = db
        db_table = 'incomes'