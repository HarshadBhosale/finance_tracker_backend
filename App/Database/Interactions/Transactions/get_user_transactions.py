from Database.Models.transactions import Transactions

def getUserTransactions(get_transactions_object):
    id = get_transactions_object["user_id"]
    transactions = Transactions.select().where(Transactions.user_id==id)
    transaction_object = []
    for transaction in transactions:
        transaction_object.append({
            "id" : transaction.id,
            "event" : transaction.event,
            "category" : transaction.category,
            "description" : transaction.description,
            "amount" : transaction.amount,
            "currency" : transaction.currency,
            "date" : transaction.date,
            "status": transaction.status
        })
    return {
        "transactions" : transaction_object
    }