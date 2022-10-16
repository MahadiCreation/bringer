from ..extensions import db
from ..f_models import Location
class location_model():
    def __init__(self) -> None:
        pass

    def add_location(obj):
        loc= Location(city=obj["city"],lat=obj["lat"],lng=obj["lng"])
        db.session.add(loc)
        db.session.flush()
        db.session.commit()
        return loc.id
        