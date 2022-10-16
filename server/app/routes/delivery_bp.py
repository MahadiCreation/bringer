from flask import Blueprint
from ..models.delivery_model import Delivery
from ..controllers.DeliveryController import *


delivery_bp=Blueprint('delivery_bp',__name__)


