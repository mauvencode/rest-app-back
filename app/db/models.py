from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class AppLocation(Base):
    __tablename__ = "app_location"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    houmer_id = Column(UUID(as_uuid=True))
    latitude = Column(Float)
    longitude = Column(Float)
    speed = Column(Integer)
    timestamp = Column(DateTime)


class Property(Base):
    __tablename__ = "property"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    geofence = Column(String)


# class Houmer(Base):
#     __tablename__ = "houmer"

#     id = Column(UUID, primary_key=True, index=True)
#     name = Column(String)
    