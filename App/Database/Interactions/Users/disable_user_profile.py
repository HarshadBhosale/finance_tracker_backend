from Database.Models.users import Users

def disableUserProfile(disable_profile_object):
    user_id = disable_profile_object["user_id"]
    is_deleted = Users.update(status=0).where(Users.id==user_id).execute()
    return is_deleted
