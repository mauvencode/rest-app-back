from sqlalchemy.orm import Session

from .models import AppLocation, Property
from datetime import date, timedelta
from uuid import UUID


def save_app_location(db: Session, houmer_id, latitude, longitude, speed, timestamp):
    db_app_location = AppLocation(
        houmer_id = houmer_id,
        latitude = latitude,
        longitude = longitude,
        speed = speed,
        timestamp = timestamp
    )
    db.add(db_app_location)
    db.commit()
    db.refresh(db_app_location)

    return db_app_location


def get_locations_by_houmer_and_date(db: Session, houmer_id: UUID, search_date: date):
    instance = (
        db.query(AppLocation)
        .filter(
            AppLocation.houmer_id == houmer_id,
            AppLocation.timestamp > search_date,
            AppLocation.timestamp < search_date + timedelta(days=1)
            )
        .all()
    )
    return instance


def get_property_list(db: Session):
    return db.query(Property).all()


def get_property_by_id(db: Session, id):
    return db.query(Property).filter_by(id=id).one_or_none()

def save_property(db: Session, id, name, latitude, longitude, geofence):
    instance = None
    if id != None:
        instance = (
            db.query(Property).filter_by(id=id).one_or_none()
        )
        if instance:
            instance.name = name
            instance.latitude = latitude
            instance.longitude = longitude
            instance.geofence = geofence
            db.commit()
            db.refresh(instance)
        else:
            instance = Property(
                id = id,
                name = name,
                latitude = latitude,
                longitude = longitude,
                geofence = geofence
            )
            db.add(instance)
            db.commit()
            db.refresh(instance)
    else:
        instance = Property(
                name = name,
                latitude = latitude,
                longitude = longitude,
                geofence = geofence
            )
        db.add(instance)
        db.commit()
        db.refresh(instance)

    return instance
