from Database.Interactions.Users.user_stats import userStats
from Database.Models.transactions import Transactions
from peewee import fn

def userGraphics(graphics_object):
    if "user_id" not in graphics_object:
        return { "message" : "user_id not provided" }
    
    user_id = graphics_object["user_id"]
    
    stats_object = {
        "user_id" : user_id,
    }
    visual_stats = {}
    
    for transaction in Transactions.select(fn.date_part('year', Transactions.date).alias('Year')).where(Transactions.user_id == user_id, Transactions.status==1).distinct():
        stats_object["year"] = transaction.Year
        visual_stats[int(transaction.Year)] = userStats(stats_object)
    
    return visual_stats