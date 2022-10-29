from Database.Models.users import Users

def updateUserProfile(update_object):
    user_id = update_object.pop("user_id")
    is_updated = Users.update(**update_object).where(Users.id==user_id).execute()
    return is_updated