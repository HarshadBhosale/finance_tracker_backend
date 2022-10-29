from Database.Models.transactions import Transactions

def updateUserTransaction(update_user_transaction_object):
    transaction_id = update_user_transaction_object.pop("transaction_id")
    is_updated = Transactions.update(**update_user_transaction_object).where(Transactions.id==transaction_id).execute()
    return is_updated