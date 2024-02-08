from Database.Models.users import Users


def updateUserProfile(update_profile_object):
    if "user_id" not in update_profile_object:
        return {"message": "user_id not provided"}

    user_id = update_profile_object.pop("user_id")
    profile_object = {}

    for field in ["name", "country_code", "mobile_number"]:
        if field in update_profile_object:
            profile_object[field] = update_profile_object[field]

    if profile_object == {}:
        return {"message": "Nothing to update"}

    if is_updated := (
        Users.update(**profile_object)
        .where(Users.id == user_id, Users.status == 1)
        .execute()
    ):
        return {"message": "Profile updated"}

    return {"message": "Profile not updated"}
