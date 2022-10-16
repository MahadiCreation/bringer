from flask import Blueprint
from ..models.notification_model import Notification
from ..controllers.NotificationController import *

notification_bp=Blueprint('notification_bp',__name__)
