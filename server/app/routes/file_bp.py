from flask import Blueprint
from ..models.file_model import File
from ..controllers.FileController import *

file_bp = Blueprint('file_bp',__name__)
file_bp.route('/send',methods=['GET'])