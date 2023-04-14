from Database.Interactions.Users.user_stats import userStats
from peewee import fn
from Database.Interactions.Transactions.get_user_transaction_years import (
    getUserTransactionYears,
)


def userGraphics(graphics_object):
    if "user_id" not in graphics_object:
        return {"message": "user_id not provided"}

    user_id = graphics_object["user_id"]

    stats_object = {
        "user_id": user_id,
    }

    transactionYears_object = {
        "user_id": user_id,
    }
    transactionYears = getUserTransactionYears(transactionYears_object)

    visual_stats = {}

    for year in transactionYears["transactionYears"]:
        stats_object["year"] = year
        visual_stats[year] = userStats(stats_object)

    return visual_stats
