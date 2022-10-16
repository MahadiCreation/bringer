from audioop import add
from flask import Blueprint
from flask import request
from ..controllers.UserController import add, retrieve, login
from ..models.user_model import User

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/user', methods=['GET'])(retrieve)
user_bp.route('/user', methods=['POST'])(add)
user_bp.route('/login', methods=['POST'])(login)
