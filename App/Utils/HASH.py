def HASH(password):
    hashed_password = ""
    for i in password:
        hashed_password = i + hashed_password
    return hashed_password
