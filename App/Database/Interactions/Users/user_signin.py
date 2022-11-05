from HASH import HASH
from Database.Models.users import Users

def userSignIn(signin_object):
    user_email = signin_object["email"]
    user_password = HASH(signin_object["password"])
    user = Users.select().where(Users.email==user_email, Users.password==user_password).first()
    return {
        "id" : user.id
    }