from flask import Blueprint
from ..models.subscription_model import Subscription
from ..controllers.SubscriptionController import *

subscription_bp  =Blueprint('subscription_bp',__name__)
