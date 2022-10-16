from operator import gt
import re


def validate_email(str):
    return re.search(str, "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")


def validate_phone(str):
    return re.search(str, "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")


def validate_num_between(num, min, max):
    if (num >= min) and (num <= max):
        return True
    else:
        return False


def validate_string_without_chars(str):
    return re.search(str, "^[a-zA-Z][a-zA-Z ]*$")


def validate_username(username):
    return re.search(username, "^[a-z0-9_-]{3,15}$")

