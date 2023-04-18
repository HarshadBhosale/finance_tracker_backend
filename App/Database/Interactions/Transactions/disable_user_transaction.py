from Database.Models.transactions import Transactions


def disableUserTransaction(disable_transaction_object):
    if "transaction_id" not in disable_transaction_object:
        return {"message": "transaction_id not provided"}

    transaction_id = disable_transaction_object["transaction_id"]
    is_deleted = (
        Transactions.update(status=0)
        .where(Transactions.id == transaction_id, Transactions.status == 1)
        .execute()
    )
    if is_deleted == 1:
        return {"message": "Transaction has been disabled"}

    return {"message": "Transaction couldn't disabled"}
