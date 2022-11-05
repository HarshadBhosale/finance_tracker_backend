from Database.Models.transactions import Transactions

def disableUserTransaction(disable_transaction_object):
    transaction_id = disable_transaction_object["transaction_id"]
    is_deleted = Transactions.update(status=0).where(Transactions.id==transaction_id).execute()
    return is_deleted