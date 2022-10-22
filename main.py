import datetime
import uuid
from fastapi import FastAPI
from pydantic import BaseModel

finance_tracker_api = FastAPI()

class Expense(BaseModel):
    id:uuid.UUID
    Category: str
    Description: str = None
    Amount: int
    Currency: str = "Rs"
    Date: datetime.datetime

class Income(BaseModel):
    id:uuid.UUID
    Category: str
    Description: str = None
    Amount: int
    Currency: str = "Rs"
    Date: datetime.datetime 

@finance_tracker_api.get("/")
def root():
    return {"Finance Tracker API": "0.0.1"}

# expense
@finance_tracker_api.get("/expenses")
def getAllExpenses():
    return {"All expenses": ["1", "2"]}

@finance_tracker_api.post("/expenses/create")
def createExpense(expense: Expense):
    return {"Expense ": "created"}

@finance_tracker_api.get("/expenses/get/{id}")
def getExpense(id: uuid.UUID):
    return {f"Expense No. {id}": "readed"}

@finance_tracker_api.post("/expenses/update/{id}")
def updateExpense(id: uuid.UUID):
    return {"Expense ": "updated"}

@finance_tracker_api.post("/expenses/delete/{id}")
def deleteExpense(id: uuid.UUID):
    return {"Expense ": "deleted"}

# income
@finance_tracker_api.get("/incomes")
def getAllIncomes():
    return {"All incomes": ["1", "2"]}

@finance_tracker_api.post("/incomes/create")
def createIncome():
    return {"Income ": "created"}

@finance_tracker_api.get("/incomes/get/{id}")
def getIncome(id: uuid.UUID):
    return {f"Income No. {id}": "readed"}

@finance_tracker_api.post("/incomes/update/{id}")
def updateIncome(id: uuid.UUID):
    return {"Income ": "updated"}

@finance_tracker_api.post("/incomes/delete/{id}")
def deleteIncome(id: uuid.UUID):
    return {"Income ": "deleted"}
