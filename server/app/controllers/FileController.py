from flask import request 
from ..extensions import db
from ..models.file_model import File
from ..utils.sms_messages import sms_messages

def send():
    return sms_messages.custom_sms()