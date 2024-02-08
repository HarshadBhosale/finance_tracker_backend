from Database.Models.transactions import Transactions


def updateUserTransaction(update_transaction_object):
    if "transaction_id" not in update_transaction_object:
        return {"message": "transaction_id not provided"}

    transaction_id = update_transaction_object["transaction_id"]
    transaction_object = {}

    for field in ["event", "category", "description", "amount", "currency", "date"]:
        if field in update_transaction_object:
            transaction_object[field] = update_transaction_object[field]

    if transaction_object == {}:
        return {"message": "Nothing to update"}

    if is_updated := (
        Transactions.update(**transaction_object)
        .where(Transactions.id == transaction_id, Transactions.status == 1)
        .execute()
    ):
        return {"message": "Transaction updated"}

    return {"message": "Transaction couldn't updated"}
