from flask import Blueprint
from ..models.business_type_model import Business_type
from ..controllers.BusinessTypeController import *

business_type_bp=Blueprint('business_type_bp',__name__)


