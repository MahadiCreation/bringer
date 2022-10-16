from ..extensions import db
from ..f_models import Notification, User, User_type
from sqlalchemy import update, insert, delete
from ..utils.marshmallow import UserSchema, UserTypeSchema
from ..utils.validations import validate_num_between
import bcrypt


class user_model():
    user_schema = UserSchema(many=False)
    users_schema = UserSchema(many=True)
    user_types_schema = UserTypeSchema(many=True)

    def login_user(username):
        res = User.query.filter_by(username=username).first()
        res = user_model.user_schema.dump(res)
        return res

    def get_users_by_id(user_id=None):
        res = User.query.filter_by(id=user_id).first()
        res = user_model.user_schema.dump(res)
        return res

    def get_users_by_username(username=None):
        res = User.query.filter_by(username=username).first()
        res = user_model.user_schema.dump(res)
        return res

    def get_all_users():
        res = db.session.query(User).all()
        res = user_model.users_schema.dump(res)
        return res

    def add_user(user):

        types = db.session.query(User_type).all()
        types = user_model.user_types_schema.dump(types, many=True)

        if not validate_num_between(user['user_type'], 1, len(types)):
            return -1
        res = user_model.get_users_by_username(user['username'])
        if len(res) > 0:
            return -2
        obj = {
            "fname": user['fname'],
            "lname": user['lname'],
            "username": user['username'],
            "email": user['email'],
            "phone": user['phone'],
            "password": user['password'],
            "user_type": user['user_type'],
            "OTP": user['OTP'],
            "is_subscribed": user['is_subscribed'],
            "subscription_id": user['subscription_id'],
            "is_delete": user['is_delete']
        }
        salt = bcrypt.gensalt(12)
        encrypted_password = bcrypt.hashpw(
            obj['password'].encode('utf8'), salt)
        user = User(fname=obj['fname'],
                    lname=obj['lname'],
                    username=obj['username'],
                    email=obj['email'],
                    phone=obj['phone'],
                    password=encrypted_password,
                    user_type=obj['user_type'],
                    OTP=obj['OTP'],
                    is_subscribed=obj['is_subscribed'],
                    subscription_id=obj['subscription_id'],
                    is_delete=obj['is_delete'],
                    )
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return user.id
