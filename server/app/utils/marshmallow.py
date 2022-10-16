from ..app import ma
from ..f_models import User,Admin,Business,Business_type,Customer,Delivery,User_type,Business_type,Location
from marshmallow_sqlalchemy.fields import Nested
from marshmallow_sqlalchemy import fields


class SmartNested(Nested):
    def serialize(self, attr, obj, accessor=None):
        if attr not in obj.__dict__:
            return {"id": int(getattr(obj, attr + "_id"))}
        return super(SmartNested, self).serialize(attr, obj, accessor)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True
        include_relationships = True
        include_fk = True 




class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Location
        load_instance=True
        include_relationships = True
        include_fk = True 
    
    

    
class BusinessSchema(ma.SQLAlchemyAutoSchema):
    user = fields.Nested(UserSchema, many=False,exclude=('password','notifications'))
    location = fields.Nested(LocationSchema, many=False)
    class Meta:
        model=Business
        load_instance=True
        include_relationships = False
        include_fk = True 
    

    
class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=User_type
        load_instance=True
        include_relationships = True
        include_fk = True 

class BusinessTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Business_type
        load_instance=True
        include_fk=True

class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Admin
        load_instance=True
        include_relationships = True
        include_fk = True 




class Business_typeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Business_type
        load_instance=True
        include_relationships = True
        include_fk = True 



class DeliverySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Delivery
        load_instance=True
        include_relationships = True
        include_fk = True 


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Customer
        load_instance=True
        include_relationships = True
        include_fk = True 