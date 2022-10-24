import datetime
import typing
import uuid
import fastapi
import pydantic
import database
import create_tables
import HASH

finance_tracker_api = fastapi.FastAPI()
create_tables.create_not_existence_tables()

class UserModel(pydantic.BaseModel):
    name: str
    email: str
    country_code: typing.Optional[int] = None
    mobile_number: typing.Optional[int] = None
    password_hash: str

class TransactionModel(pydantic.BaseModel):
    user_id : uuid.UUID
    event: int
    category: str
    description: typing.Optional[str] = None
    amount: int
    currency: str
    date: typing.Optional[datetime.datetime] = None



@finance_tracker_api.on_event("startup")
def startup_event():
    if database.db.is_closed():
        database.db.connect()

@finance_tracker_api.on_event("shutdown")
def shutdown_event():
    if not database.db.is_closed():
        database.db.close()

@finance_tracker_api.get("/")
def root():
    version = "1.0.0"
    return {"Finance Tracker API" : version}



@finance_tracker_api.post("/users/create")
def createUser(user: UserModel):
    user_object = {
        "id" : uuid.uuid4(),
        "name" : user.name,
        "email" : user.email,
        "country_code" : user.country_code,
        "mobile_number" : user.mobile_number,
        "password_hash" : HASH.HASH(user.password_hash),
        "status": 1,
        "created_at" : datetime.datetime.now(),
        "updated_at" : datetime.datetime.now()
    }
    database.Users.create(**user_object)
    return {
        "id" : user_object["id"]
    }

@finance_tracker_api.get("/users/get")
def getUser(get_object: dict):
    id = get_object.pop("user_id")
    user = database.Users.select().where(database.Users.id==id).get()
    user_object = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "country_code": user.country_code,
        "mobile_number": user.mobile_number,
        "password_hash": user.password_hash,
        "status": user.status
    }
    return user_object

@finance_tracker_api.post("/users/update")
def updateUser(update_object: dict):
    if "password_hash" in update_object:
        update_object["password_hash"] = HASH.HASH(update_object["password_hash"])
    user_id = update_object.pop("user_id")
    is_updated = database.Users.update(**update_object).where(database.Users.id==user_id).execute()
    return is_updated

@finance_tracker_api.post("/users/delete")
def deleteUser(delete_object: dict):
    user_id = delete_object.pop("user_id")
    is_deleted = database.Users.update(status=0).where(database.Users.id==user_id).execute()
    return is_deleted



@finance_tracker_api.get("/transactions")
def getAllTransactions(get_all_object: dict):
    id = get_all_object.pop("user_id")
    transactions = database.Transactions.select().where(database.Transactions.user_id==id)
    transaction_object = []
    for transaction in transactions:
        transaction_object.append({
            "id" : transaction.id,
            "event" : transaction.event,
            "category" : transaction.category,
            "description" : transaction.description,
            "amount" : transaction.amount,
            "currency" : transaction.currency,
            "date" : transaction.date,
            "status": transaction.status
        })
    return {"transactions" : transaction_object}

@finance_tracker_api.post("/transactions/create")
def createTransaction(transaction: TransactionModel):
    transaction_object = {
        "id" : uuid.uuid4(),
        "user_id" : transaction.user_id,
        "event" : transaction.event,
        "category" : transaction.category,
        "description" : transaction.description,
        "amount" : transaction.amount,
        "currency" : transaction.currency,
        "date" : transaction.date if transaction.date else datetime.datetime.now(),
        "status": 1,
        "created_at" : datetime.datetime.now(),
        "updated_at" : datetime.datetime.now()
    }
    database.Transactions.create(**transaction_object)
    return {
        "id" : transaction_object["id"]
    }

@finance_tracker_api.get("/transactions/get")
def getTransaction(get_object: dict):
    id = get_object.pop("transaction_id")
    transaction = database.Transactions.select().where(database.Transactions.id==id).get()
    transaction_object = {
        "id" : transaction.id,
        "user_id" : transaction.user_id,
        "event" : transaction.event,
        "category" : transaction.category,
        "description" : transaction.description,
        "amount" : transaction.amount,
        "currency" : transaction.currency,
        "date" : transaction.date,
        "status": transaction.status
    }
    return transaction_object

@finance_tracker_api.post("/transactions/update")
def updateTransaction(update_object: dict):
    transaction_id = update_object.pop("transaction_id")
    is_updated = database.Transactions.update(**update_object).where(database.Transactions.id==transaction_id).execute()
    return is_updated

@finance_tracker_api.post("/transactions/delete")
def deleteTransaction(delete_object: dict):
    transaction_id = delete_object.pop("transaction_id")
    is_deleted = database.Transactions.update(status=0).where(database.Transactions.id==transaction_id).execute()
    return is_deleted