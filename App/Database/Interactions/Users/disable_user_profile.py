from Database.Models.users import Users


def disableUserProfile(disable_profile_object):
    if "user_id" not in disable_profile_object:
        return {"message": "user_id not provided"}

    user_id = disable_profile_object["user_id"]

    is_deleted = (
        Users.update(status=0).where(Users.id == user_id, Users.status == 1).execute()
    )
    if is_deleted:
        return {"message": "Your account was disabled"}

    return {"message": "Account couldn't be disabled"}
