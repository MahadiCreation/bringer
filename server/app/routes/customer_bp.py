from flask import Blueprint
from ..models.customer_model import Customer
from ..controllers.CustomerController import *


customer_bp=Blueprint('customer_bp',__name__)


