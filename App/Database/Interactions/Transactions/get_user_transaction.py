from Database.Models.transactions import Transactions

def getUserTransaction(get_transaction_object):
    id = get_transaction_object["transaction_id"]
    transaction = Transactions.select().where(Transactions.id==id).get()
    transaction_object = {
        "id" : transaction.id,
        "user_id" : transaction.user_id,
        "event" : transaction.event,
        "category" : transaction.category,
        "description" : transaction.description,
        "amount" : transaction.amount,
        "currency" : transaction.currency,
        "date" : transaction.date,
        "status": transaction.status
    }
    return transaction_object