from Database.Models.users import Users

def deleteUserProfile(delete_object: dict):
    user_id = delete_object["user_id"]
    is_deleted = Users.update(status=0).where(Users.id==user_id).execute()
    return is_deleted
