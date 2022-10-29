from Database.Models.users import Users
from HASH import HASH

def updateUserProfilePassword(update_object):
    user_id = update_object.pop("user_id")
    update_object["password_hash"] = HASH(update_object["password_hash"])
    is_updated = Users.update(**update_object).where(Users.id==user_id).execute()
    return is_updated