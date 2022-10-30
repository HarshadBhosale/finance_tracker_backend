from Database.Models.users import Users
from HASH import HASH

def updateUserProfilePassword(user_object):
    user_id = user_object.pop("user_id")
    user_object["password"] = HASH(user_object["password"])
    is_updated = Users.update(**user_object).where(Users.id==user_id).execute()
    return is_updated