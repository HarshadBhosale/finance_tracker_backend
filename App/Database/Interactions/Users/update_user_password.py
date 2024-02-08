from Database.Models.users import Users
from Utils.HASH import HASH


def updateUserPassword(update_password_object):
    if "user_id" not in update_password_object:
        return {"message": "user_id not provided"}

    if "password" not in update_password_object:
        return {"message": "password not provided"}

    user_id = update_password_object.pop("user_id")

    update_password_object["password"] = HASH(update_password_object["password"])
    if is_updated := (
        Users.update(**update_password_object)
        .where(Users.id == user_id, Users.status == 1)
        .execute()
    ):
        return {"message": "Account password updated"}

    return {"message": "Account password couldn't be updated"}
