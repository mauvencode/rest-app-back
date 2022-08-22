from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from fastapi_camelcase import CamelModel


class AppLocationDto(CamelModel):
    houmer_id: UUID
    latitude: float
    longitude: float
    speed: int
    timestamp: datetime


class VisitedPlace(CamelModel):
    property_id: UUID
    latitude: float
    longitude: float
    duration: int


class VisitedPlaceResponseDto(CamelModel):
    houmer_id: UUID
    search_date: date
    places: list[VisitedPlace] | None = None


class HighSpeedMoment(CamelModel):
    timestamp: datetime
    speed: int
    app_location_id: UUID


class HighSpeedMomentResponseDto(CamelModel):
    houmer_id: UUID
    search_date: date
    speed_limit: int
    moments: list[HighSpeedMoment] | None = None


class PropertyDto(CamelModel):
    id: Optional[UUID]
    name: str
    latitude: float
    longitude: float
    geofence: Optional[str]
