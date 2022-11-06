from Database.Models.transactions import Transactions

def getUserTransactions(get_transactions_object):
    if "user_id" not in get_transactions_object:
        return { "message" : "user_id not provided" }
    
    id = get_transactions_object["user_id"]
    transactions = Transactions.select().where(Transactions.user_id==id, Transactions.status==1)
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
        })
    return {
        "transactions" : transaction_object
    }