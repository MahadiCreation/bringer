from ..f_models import Business, Business_type
from ..utils.marshmallow import BusinessSchema
from ..extensions import db

#business functions 
#see open orders
#add a new order
#update personal information
#check statistics
class business_model():
    single_business_schema = BusinessSchema(many=False)
    business_schema = BusinessSchema(many=True)



    def add_business(obj):
        business= Business(id=obj['user_id'],business_type=obj['business_type'],location_id=obj['location_id'],is_delete=0)
        db.session.add(business)
        db.session.flush()
        db.session.commit()
        return business.id



    def get_business(id):
        if id:
            res= db.session.query(Business).filter(Business.id==id).first()
            res = business_model.single_business_schema.dump(res)
        else : 
            res= db.session.query(Business).all()
            res = business_model.business_schema.dump(res)

        
        return res






    def AddOrder():
        
        return True

    def UpdatePInfo():

        return True
    def ChangePassword():
        return True

    def CheckOrders():
        return True

    def CheckStatistics():
        return True



