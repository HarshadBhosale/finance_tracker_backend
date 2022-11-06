from Database.Models.users import Users

def userProfile(profile_object):
    id = profile_object["user_id"]
    users = Users.select().where(Users.id==id, Users.status==1).execute()
    for user in users:
        user_object = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "country_code": user.country_code,
            "mobile_number": user.mobile_number,
            "user_session" : user.user_session,
            "status": user.status
        }
        return user_object
    return {"message" : "No user found"}