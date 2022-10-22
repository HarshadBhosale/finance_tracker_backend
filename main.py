import datetime
import uuid
import fastapi
import pydantic
import database
import create_tables

finance_tracker_api = fastapi.FastAPI()

class UserModel(pydantic.BaseModel):
    name: str
    email: str
    country_code: int
    mobile_number: int
    password_hash: str

class TransactionModel(pydantic.BaseModel):
    Event: int
    Category: str
    Description: str = None
    Amount: int
    Currency: str
    Date: datetime.datetime



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
    return {"Finance Tracker API": "0.1.0"}



@finance_tracker_api.get("/users")
def getAllUsers():
    return {"All users": ["1", "2"]}

@finance_tracker_api.post("/users/create")
def createUser(user: UserModel):
    return {"User ": "created"}

@finance_tracker_api.get("/users/get/{id}")
def getUser(id: uuid.UUID):
    return {f"User No. {id}": "readed"}

@finance_tracker_api.post("/users/update/{id}")
def updateUser(id: uuid.UUID):
    return {"User ": "updated"}

@finance_tracker_api.post("/users/delete/{id}")
def deleteUser(id: uuid.UUID):
    return {"User ": "deleted"}



@finance_tracker_api.get("/transactions")
def getAllTransactions():
    return {"All transactions": ["1", "2"]}

@finance_tracker_api.post("/transactions/create")
def createTransaction(transaction: TransactionModel):
    return {"Transaction ": "created"}

@finance_tracker_api.get("/transactions/get/{id}")
def getTransaction(id: uuid.UUID):
    return {f"Transaction No. {id}": "readed"}

@finance_tracker_api.post("/transactions/update/{id}")
def updateTransaction(id: uuid.UUID):
    return {"Transaction ": "updated"}

@finance_tracker_api.post("/transactions/delete/{id}")
def deleteTransaction(id: uuid.UUID):
    return {"Transaction ": "deleted"}