from Database.Models.transactions import Transactions
from peewee import fn

def getUserStats(user_object):
    id = user_object["user_id"]
    all_transactions = Transactions.select(fn.date_part('year', Transactions.date).alias('Year'), fn.date_part('month', Transactions.date).alias('Month'), Transactions.event, Transactions.category, fn.SUM(Transactions.amount).alias('Amount')).where(Transactions.user_id==id).group_by(fn.date_part('year', Transactions.date), fn.date_part('month', Transactions.date), Transactions.event, Transactions.category)
    stats_object = {}
    for transaction in all_transactions:
        Event = "Expense" if transaction.event == -1 else "Income"
        stats_object.setdefault(int(transaction.Year), {}).setdefault(int(transaction.Month), {}).setdefault(Event, {}).setdefault(transaction.category, transaction.Amount)
        stats_object[transaction.Year]["Total " + Event] = stats_object[transaction.Year].get("Total " + Event, 0) + transaction.Amount
        stats_object[transaction.Year][transaction.Month]["Total " + Event] = stats_object[transaction.Year][transaction.Month].get("Total " + Event, 0) + transaction.Amount
    if "Year" in user_object:
        return stats_object[user_object["Year"]]
    return stats_object