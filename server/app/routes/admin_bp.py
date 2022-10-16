from flask import Blueprint
from ..models.admin_model import Admin
from ..controllers.AdminController import *

admin_bp=Blueprint('admin_bp',__name__)

