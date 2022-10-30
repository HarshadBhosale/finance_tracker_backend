from Database.Models.users import Users

def updateUserProfile(user_object):
    user_id = user_object.pop("user_id")
    is_updated = Users.update(**user_object).where(Users.id==user_id).execute()
    return is_updated