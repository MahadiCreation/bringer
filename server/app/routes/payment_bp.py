from flask import Blueprint
from ..models.payment_model import Payment
from ..controllers.PaymentController import *


payment_bp=Blueprint('payment_bp',__name__)
