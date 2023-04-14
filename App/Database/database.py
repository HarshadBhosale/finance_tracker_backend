from peewee import PostgresqlDatabase
from Helper import env

database = PostgresqlDatabase(
    env.DATABASE_NAME,
    autorollback=True,
    user=env.DATABASE_USER_NAME,
    password=env.DATABASE_PASSWORD,
    host=env.DATABASE_HOST,
    port=env.DATABASE_PORT,
)
