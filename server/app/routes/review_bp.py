from flask import Blueprint
from ..controllers.ReviewsController import  *
from ..models.review_model import Review

review_bp = Blueprint('review_bp', __name__)


