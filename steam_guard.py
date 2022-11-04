from steampy.guard import generate_one_time_code

def getCode(secret):
    shared_secret = secret
    authentication_code = generate_one_time_code(shared_secret)

    return authentication_code