from Database.Models.transactions import Transactions


def getUserTransaction(get_transaction_object):
    if "transaction_id" not in get_transaction_object:
        return {"message": "transaction_id not provided"}

    id = get_transaction_object["transaction_id"]
    transactions = (
        Transactions.select()
        .where(Transactions.id == id, Transactions.status == 1)
        .execute()
    )
    for transaction in transactions:
        transaction_object = {
            "id": transaction.id,
            "user_id": transaction.user_id,
            "event": transaction.event,
            "category": transaction.category,
            "description": transaction.description,
            "amount": transaction.amount,
            "currency": transaction.currency,
            "date": transaction.date,
        }
        return transaction_object

    return {"message": "No transaction found"}
