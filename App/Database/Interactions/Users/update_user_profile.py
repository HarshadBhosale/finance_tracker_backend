from Database.Models.users import Users

def updateUserProfile(update_profile_object):
    user_id = update_profile_object.pop("user_id")
    is_updated = Users.update(**update_profile_object).where(Users.id==user_id).execute()
    return is_updated