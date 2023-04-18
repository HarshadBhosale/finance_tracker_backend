from Database.Models.transactions import Transactions
from uuid import uuid4
from datetime import datetime


def createUserTransaction(transaction):
    transaction_object = {
        "id": uuid4(),
        "user_id": transaction.user_id,
        "event": transaction.event,
        "category": transaction.category,
        "description": transaction.description,
        "amount": transaction.amount,
        "currency": transaction.currency,
        "date": transaction.date if transaction.date else datetime.now(),
        "status": 1,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    Transactions.create(**transaction_object)
    return {"id": transaction_object["id"]}
