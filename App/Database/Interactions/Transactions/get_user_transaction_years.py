from Database.Models.transactions import Transactions
from peewee import fn

def getUserTransactionYears(get_transaction_object):
    if "user_id" not in get_transaction_object:
        return { "message" : "user_id not provided" }
    
    user_id = get_transaction_object["user_id"]
    transactionYears = []
    transactions = Transactions.select(fn.date_part('year', Transactions.date).alias('Year')).where(Transactions.user_id == user_id, Transactions.status==1).distinct().execute()
    for transaction in transactions:
        transactionYears.append(int(transaction.Year))
    
    if transactionYears != []:
        return { "transactionYears" : transactionYears }
    
    return { "message" : "No transaction found" }