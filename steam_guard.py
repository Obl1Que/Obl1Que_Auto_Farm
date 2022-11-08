from steampy.guard import generate_one_time_code

def getCode(shared_secret):
    return generate_one_time_code(shared_secret)