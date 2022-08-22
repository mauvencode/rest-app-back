from app.db.repositories import (
    get_property_list, 
    get_property_by_id,
    save_property
    )
from app.schemas import PropertyDto

class PropertyService():

    def get_property(self, db, id):
        property = get_property_by_id(db, id)
        return property

    def save_property(self, db, property_dto: PropertyDto):
        property = save_property(
            db, 
            property_dto.id,
            property_dto.name,
            property_dto.latitude,
            property_dto.longitude,
            property_dto.geofence
            )
        return property
