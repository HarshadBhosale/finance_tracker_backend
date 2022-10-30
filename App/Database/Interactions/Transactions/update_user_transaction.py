from Database.Models.transactions import Transactions

def updateUserTransaction(user_transaction_object):
    transaction_id = user_transaction_object.pop("transaction_id")
    is_updated = Transactions.update(**user_transaction_object).where(Transactions.id==transaction_id).execute()
    return is_updated