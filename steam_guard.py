from steampy.guard import generate_one_time_code
from json import load

def getCode(path):
    shared_secret = load(open(path))["shared_secret"]
    authentication_code = generate_one_time_code(shared_secret)

    return authentication_code