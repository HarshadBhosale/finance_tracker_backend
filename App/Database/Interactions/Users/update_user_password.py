from Database.Models.users import Users
from HASH import HASH

def updateUserPassword(update_password_object):
    user_id = update_password_object.pop("user_id")
    update_password_object["password"] = HASH(update_password_object["password"])
    is_updated = Users.update(**update_password_object).where(Users.id==user_id).execute()
    return is_updated