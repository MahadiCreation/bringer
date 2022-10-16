from flask import Blueprint
from ..models.location_model import Location
from ..controllers.LocationController import *

location_bp=Blueprint('location_bp',__name__)

