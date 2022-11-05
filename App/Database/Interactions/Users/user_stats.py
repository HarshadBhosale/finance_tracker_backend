from Database.Models.transactions import Transactions
from peewee import fn

def userStats(stats_object):
    id = stats_object["user_id"]
    all_transactions = Transactions.select(fn.date_part('year', Transactions.date).alias('Year'), fn.date_part('month', Transactions.date).alias('Month'), Transactions.event, Transactions.category, fn.SUM(Transactions.amount).alias('Amount')).where(Transactions.user_id==id).group_by(fn.date_part('year', Transactions.date), fn.date_part('month', Transactions.date), Transactions.event, Transactions.category)
    stats = {}
    for transaction in all_transactions:
        Event = "Expense" if transaction.event == -1 else "Income"
        stats.setdefault(int(transaction.Year), {}).setdefault(int(transaction.Month), {}).setdefault(Event, {}).setdefault(transaction.category, transaction.Amount)
        stats[transaction.Year]["Total " + Event] = stats[transaction.Year].get("Total " + Event, 0) + transaction.Amount
        stats[transaction.Year][transaction.Month]["Total " + Event] = stats[transaction.Year][transaction.Month].get("Total " + Event, 0) + transaction.Amount
    if "Year" in stats_object:
        return stats[stats_object["Year"]]
    return stats