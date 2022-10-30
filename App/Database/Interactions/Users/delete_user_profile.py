from Database.Models.users import Users

def deleteUserProfile(user_object: dict):
    user_id = user_object["user_id"]
    is_deleted = Users.update(status=0).where(Users.id==user_id).execute()
    return is_deleted
