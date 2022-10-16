from datetime import date, datetime
import jwt
from datetime import timedelta


def get_token(obj):
    obj["exp"] = datetime.now() + timedelta(5)
    encoded_jwt = jwt.encode(obj, "Metallica666", algorithm="HS256")
    return encoded_jwt

def get_token_with_exp(obj,days,hours):
    obj["exp"] = datetime.now() + timedelta(days=days,hours=hours)
    encoded_jwt = jwt.encode(obj, "Metallica666", algorithm="HS256")
    return encoded_jwt