from Database.Models.transactions import Transactions
from uuid import uuid4
from datetime import datetime

def createUserTransaction(user_transaction_object):
    transaction_object = {
        "id" : uuid4(),
        "user_id" : user_transaction_object.user_id,
        "event" : user_transaction_object.event,
        "category" : user_transaction_object.category,
        "description" : user_transaction_object.description,
        "amount" : user_transaction_object.amount,
        "currency" : user_transaction_object.currency,
        "date" : user_transaction_object.date if user_transaction_object.date else datetime.datetime.now(),
        "status": 1,
        "created_at" : datetime.now(),
        "updated_at" : datetime.now()
    }
    Transactions.create(**transaction_object)
    return {
        "id" : transaction_object["id"]
    }