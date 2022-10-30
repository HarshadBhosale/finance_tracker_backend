from Database.Models.transactions import Transactions

def deleteUserTransaction(user_transaction_object):
    transaction_id = user_transaction_object["transaction_id"]
    is_deleted = Transactions.update(status=0).where(Transactions.id==transaction_id).execute()
    return is_deleted