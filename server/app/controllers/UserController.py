
from ..utils.helpers import custom_error
import json
from ..models.user_model import user_model
from ..models.user_type_model import User_type
from ..extensions import db
from flask import request, jsonify
from ..utils.generate import get_token_with_exp
import bcrypt


def retrieve():
    id = request.args.get('id')
    username = request.args.get('username')
    if id:
        result = user_model.get_users_by_id(id)
    elif username:
        result = user_model.get_users_by_username(username)
    else:
        result = user_model.get_all_users()
    message = {
        "status": True if result else False,
        "message": result if result else "No Users"
    }
    return jsonify(message)


def add():
    input = request.get_json()
    if not ("fname" in input and "lname" in input and "username" in input and "phone" in input and "password" in input and "user_type" in input):
        response = custom_error(
            "Some of the required fields not provided", 400)

        return response

    obj = {
        "fname": input['fname'],
        "lname": input['lname'],
        "username": input['username'],
        "email": input['email'] if input['email'] else None,
        "phone": input['phone'],
        "password": input['password'],
        "user_type": input['user_type'],
        "OTP": input['OTP'] if input['OTP'] else None,
        "is_subscribed": 0,
        "subscription_id": None,
        "is_delete": 0
    }
    
    user_id = user_model.add_user(obj)
    if user_id == -1:
        message = "no such a user_type"
    elif user_id== -2:
        message = "Username already exists"
    else:
        message = "user has been added"
    response = {
        "status": True,
        "user_id": user_id,
        "message": message

    }
    return jsonify(response)


def login():
    input = request.get_json()
    if not ("username" in input and "password" in input):
        message = {
            "status": False,
            "message": "Some of the required fields not provided"
        }
        return custom_error(message, 400)

    result = user_model.login_user(input['username'])
    if not (bcrypt.checkpw(str(input['password']).encode('UTF-8'), result['password'].encode('UTF-8'))):
        message = {
            "status": False,
            "message": "incorrect username or password "
        }
        return custom_error(message, 404)
    else:
        obj = {
            "username": result['username'],
            "fname": result['fname'],
            "lname": result['lname'],
            "user_type": result['user_type']
        }
        jwt_token = get_token_with_exp(obj, 30, 0)
        message = {
            "status": True,
            "message": "login successfully",
            "token": jwt_token
        }
        return custom_error(message, 200)
