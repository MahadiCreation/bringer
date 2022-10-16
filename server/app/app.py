from decimal import Decimal
from distutils.command.config import config
from flask_marshmallow import Marshmallow
from flask import Flask
from .extensions import db,migrate,ma
from .routes.review_bp import review_bp
from .routes.user_bp import user_bp
from .routes.admin_bp import admin_bp
from .routes.business_bp import business_bp
from .routes.business_type_bp import business_type_bp
from .routes.customer_bp import customer_bp
from .routes.delivery_bp import delivery_bp
from .routes.delivery_person_bp import delivery_person_bp
from .routes.file_bp import file_bp
from .routes.location_bp import location_bp
from .routes.notification_bp import notification_bp
from .routes.notification_status_bp import notification_status_bp
from .routes.payment_bp import payment_bp
from .routes.subscription_bp import subscription_bp
from .routes.subscription_plan_bp import subscription_plan_bp
from .routes.user_type_bp import user_type_bp
from . import config
from .models.user_model import User
import json






def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    Marshmallow.init_app(ma,app)
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(review_bp, url_prefix='/review')
    app.register_blueprint(business_bp, url_prefix='/business')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(business_type_bp,url_prefix='/business_type')
    app.register_blueprint(customer_bp,url_prefix='/customer')
    app.register_blueprint(delivery_bp,url_prefix='/delivery')
    app.register_blueprint(delivery_person_bp,url_prefix='/delivery_person')
    app.register_blueprint(file_bp,url_prefix='/file')
    app.register_blueprint(location_bp,url_prefix='/location')
    app.register_blueprint(notification_bp,url_prefix='/notification')
    app.register_blueprint(notification_status_bp,url_prefix='/notification_status')
    app.register_blueprint(payment_bp,url_prefix='/payment')
    app.register_blueprint(subscription_bp,url_prefix='/subscription')
    app.register_blueprint(subscription_plan_bp,url_prefix='/subscription_plan')
    app.register_blueprint(user_type_bp,url_prefix='/user_type')

    print("started")
    
    return app



# if __name__ == '__main__':
#     app.debug = True
#     app.run()