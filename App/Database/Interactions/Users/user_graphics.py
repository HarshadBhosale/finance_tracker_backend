from Database.Interactions.Users.user_stats import userStats

def userGraphics(graphics_object):
    stats_object = userStats(graphics_object)
    visual_stats_object = stats_object
    return visual_stats_object