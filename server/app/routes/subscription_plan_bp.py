from sys import builtin_module_names
from flask import Blueprint
from ..models.subscription_plan_model import Subscription_plan
from ..controllers.SubscriptionPlanController import *



subscription_plan_bp=Blueprint("subscription_plan_bp",__name__)
