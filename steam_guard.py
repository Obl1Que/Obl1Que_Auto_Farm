from steampy.guard import generate_one_time_code

def getcode(secret):
    shared_secret = secret
    authentication_code = generate_one_time_code(shared_secret)

    return authentication_code