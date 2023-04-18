from Database.Models.transactions import Transactions
from peewee import fn


def userStats(stats_object):
    if "user_id" not in stats_object:
        return {"message": "user_id not provided"}

    if "year" not in stats_object:
        return {"message": "year for stats not provided"}

    user_id = stats_object["user_id"]
    year = stats_object["year"]

    months = {
        1: "jan",
        2: "feb",
        3: "mar",
        4: "apr",
        5: "may",
        6: "june",
        7: "july",
        8: "aug",
        9: "sept",
        10: "oct",
        11: "nov",
        12: "dec",
    }

    stats = {
        "Total Income": 0,
        "Total Expense": 0,
    }
    for month in months:
        stats[months[month]] = {
            "Income": {
                "Salary": 0,
                "Investments": 0,
                "Business": 0,
            },
            "Expense": {
                "Food": 0,
                "Grocery": 0,
                "Gift": 0,
                "Family": 0,
                "Transport": 0,
                "Rent": 0,
                "EMI": 0,
                "Electricity": 0,
                "Subscription": 0,
                "Other": 0,
            },
            "Total Income": 0,
            "Total Expense": 0,
        }

    all_transactions = (
        Transactions.select(
            fn.date_part("month", Transactions.date).alias("Month"),
            Transactions.event,
            Transactions.category,
            fn.SUM(Transactions.amount).alias("Amount"),
        )
        .where(
            Transactions.user_id == user_id,
            fn.date_part("year", Transactions.date) == year,
            Transactions.status == 1,
        )
        .group_by(
            fn.date_part("month", Transactions.date),
            Transactions.event,
            Transactions.category,
        )
    )

    for transaction in all_transactions:
        Event = "Expense" if transaction.event == -1 else "Income"
        stats[months[int(transaction.Month)]][Event][
            transaction.category
        ] = transaction.Amount

    for month in months.values():
        stats[month]["Total Income"] = sum(stats[month]["Income"].values())
        stats[month]["Total Expense"] = sum(stats[month]["Expense"].values())
        stats["Total Income"] += stats[month]["Total Income"]
        stats["Total Expense"] += stats[month]["Total Expense"]

    return stats
