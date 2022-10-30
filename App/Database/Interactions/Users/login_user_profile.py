from HASH import HASH
from Database.Models.users import Users

def loginUserProfile(login_object):
    user_email = login_object["email"]
    user_password = HASH(login_object["password"])
    user = Users.select().where(Users.email==user_email, Users.password==user_password).first()
    return {
        "id" : user.id
    }