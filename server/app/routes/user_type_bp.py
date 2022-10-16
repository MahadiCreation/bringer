from flask import Blueprint
from ..models.user_type_model import User_type
from ..controllers.UserTypeController import *

user_type_bp= Blueprint('user_type_bp',__name__)
