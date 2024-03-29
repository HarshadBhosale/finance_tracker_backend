from datetime import datetime
from uuid import uuid4
from Utils.HASH import HASH
from Database.Models.users import Users


def userSignUp(user):
    user_email = user.email
    email_in_db = Users.select().where(Users.email == user_email).count()
    if email_in_db != 0:
        return {"message": "Account with email already exists"}

    user_object = {
        "id": uuid4(),
        "name": user.name,
        "email": user.email,
        "country_code": user.country_code,
        "mobile_number": user.mobile_number,
        "password": HASH(user.password),
        "user_session": user.user_session,
        "status": 1,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    Users.create(**user_object)
    return {"id": user_object["id"]}
