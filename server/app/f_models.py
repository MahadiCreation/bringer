from collections import UserList
from .extensions import db
from sqlalchemy import TIMESTAMP
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(128))
    lname = db.Column(db.String(128))
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    password = db.Column(db.String(128))
    user_type = db.Column(db.Integer(), ForeignKey('user_type.id'))
    OTP = db.Column(db.String(500))
    is_subscribed = db.Column(db.Integer())
    subscription_id = db.Column(db.Integer(), ForeignKey('subscription.id'))
    is_delete = db.Column(db.Integer())
    notifications=db.relationship('Notification',backref="user")

    

class Admin(db.Model):
    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', uselist=False)
    role = db.Column(db.Integer())
    is_delete = db.Column(db.Integer())


class Customer(db.Model):
    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', uselist=False)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(10))
    location_id= db.Column(db.Integer(),ForeignKey('location.id'))
    location = db.relationship('Location', uselist=False)
    deliveries = db.relationship('Delivery', backref='Customer')


class Business(db.Model):
    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', uselist=False)
    business_type = db.Column(db.Integer())
    delivery = db.relationship('Delivery', backref='Business')
    location_id= db.Column(db.Integer(),ForeignKey('location.id'))
    location = db.relationship('Location', uselist=False)
    is_delete = db.Column(db.Integer())
    


class Business_type(db.Model):
    id = db.Column(db.Integer, ForeignKey('business.id'), primary_key=True)
    type = db.Column(db.Integer())
    category = db.Column(db.String(50))


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500))
    review = db.Column(db.Integer(), ForeignKey('review.id'))
    status = db.Column(db.Integer())
    dp_accepted = db.Column(db.Integer(), ForeignKey('delivery_person.id'))
    business = db.Column(db.Integer(), ForeignKey('business.id'))
    customer = db.Column(db.Integer(), ForeignKey('customer.id'))
    order_time = db.Column(TIMESTAMP)
    pick_time = db.Column(TIMESTAMP)
    delivery_time = db.Column(TIMESTAMP)
    remarks = db.Column(db.String(500))


class DeliveryPerson(db.Model):
    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    type = db.Column(db.Integer())
    status = db.Column(db.Integer())
    driving_licence = db.Column(db.Integer())
    idCard = db.Column(db.Integer())
    passport = db.Column(db.Integer())
    is_delete = db.Column(db.Integer())
    # delivery=db.relationship('delivery',backref='dp')


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    size = db.Column(db.Integer())
    type = db.Column(db.String(10))
    user_id = db.Column(db.Integer())
    created_at = db.Column(TIMESTAMP)
    s3_key = db.Column(db.String(500))
    is_delete = db.Column(db.Integer())


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50))
    lat = db.Column(db.String(50))
    lng = db.Column(db.String(50))


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(50))
    body = db.Column(db.String(500))
    timedate = db.Column(db.String(50))
    status = db.Column(db.Integer(),ForeignKey('notification_status.status_id'))
    user_id = db.Column(db.Integer(),ForeignKey('user.id'))


class Notification_status(db.Model):
    status_id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.String(50))
    notifications=db.relationship('Notification',backref="Status")


class Payment(db.Model):
    transaction_number = db.Column(db.String(500), primary_key=True)
    payment_amount = db.Column(db.Integer())
    timedate = db.Column(db.String(50))
    status = db.Column(db.String(10))


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    delivery = db.relationship('Delivery', backref='Review', uselist=False)
    business_rating = db.Column(db.Integer())
    delivery_rating = db.Column(db.Integer())
    comment = db.Column(db.String(500))


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer(), ForeignKey('subscription_plan.id'))
    users = db.relationship('User', backref='subscription',uselist=True)
    status = db.Column(db.Integer())
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    payment = db.Column(db.String(500), ForeignKey(
        'payment.transaction_number'))
    duration = db.Column(db.Integer())


class Subscription_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    price = db.Column(db.Integer())
    duration = db.Column(db.Integer())


class User_type(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.String(100))
