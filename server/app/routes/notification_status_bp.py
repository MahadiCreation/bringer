from flask import Blueprint
from ..models.notification_status_model import Notification_status
from ..controllers.NotificationStatusController import *

notification_status_bp = Blueprint("notification_status_bp",__name__)
