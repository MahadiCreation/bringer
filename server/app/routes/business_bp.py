from flask import Blueprint
from ..models.business_model import Business
from ..controllers.BusinessController import add,get_business_data

business_bp=Blueprint('business_bp',__name__)
business_bp.route('/business',methods=['POST'])(add)
business_bp.route('/business',methods=['GET'])(get_business_data)
