from Utils.HASH import HASH
from Database.Models.users import Users


def userSignIn(signin_object):
    user_email = signin_object["email"]

    if (email_in_db := Users.select().where(Users.email == user_email).count()) == 0:
        return {"message": "No account linked to email"}

    if (active_email_in_db := (
        Users.select().where(Users.email == user_email, Users.status == 1).count()
    )) == 0:
        return {"message": "Your Account has been disabled"}

    user_password = HASH(signin_object["password"])

    users = (
        Users.select()
        .where(
            Users.email == user_email,
            Users.password == user_password,
            Users.status == 1,
        )
        .execute()
    )
    for user in users:
        return {"id": user.id}

    return {"message": "Password was incorect"}
