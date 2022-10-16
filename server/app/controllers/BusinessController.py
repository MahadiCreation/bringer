from flask import request
import json
from app.utils.marshmallow import BusinessSchema
from ..extensions import db
from ..f_models import User,Business
from ..models.business_model import business_model
from ..models.business_type_model import business_type_model
from ..models.location_model import location_model
from ..utils.helpers import custom_error
from flask import jsonify
from ..models.user_model import user_model

def add():
    input = request.get_json()
    if not ("fname" in input and "lname" in input and "username" in input and "phone" in input and "password" in input and "user_type" in input and "business_type" in input and "city" in input):
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
        loc_obj={
            "city":input["city"],
            "lat":"0",
            "lng":"0"
        }
        location_id=location_model.add_location(loc_obj)
        obj ={
            "user_id": user_id,
            "business_type": input["business_type"],
            "location_id":location_id 
        }
        business_id= business_model.add_business(obj)
        message = "user has been added"
    response = {
        "status": True,
        "user_id": user_id,
        "message": message

    }
    return jsonify(response)


def get_business_data():
    id = request.args.get('id')
    res= business_model.get_business(id)
    message = {
        "status" : True,
        "data": res
        }
    return custom_error(message,200)
    