from fastapi import Depends, FastAPI, HTTPException
from os import getenv
from loguru import logger

from app.schemas import (
    AppLocationDto, 
    VisitedPlaceResponseDto, 
    HighSpeedMomentResponseDto,
    PropertyDto
    )

from app.services.location import LocationService
from app.services.property import PropertyService
from app.services.visited_places import VisitedPlacesService
from app.services.high_speed import HighSpeedService
from app.services.property import PropertyService

from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base

from uuid import UUID
from datetime import date

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/app/location/")
async def save_location(app_location_dto: AppLocationDto, db: Session = Depends(get_db)):
    saved_location = LocationService().save(db, app_location_dto)
    return saved_location


@app.get("/visited_places/houmer/{houmer_id}/date/{search_date}")
async def visited_places(houmer_id: UUID, search_date: date, db: Session = Depends(get_db)):
    logger.info(f"Search visited places at {search_date} by houmerId: {houmer_id}")
    places = VisitedPlacesService().get_visited_places(db, houmer_id, search_date)
    
    response = VisitedPlaceResponseDto(
        houmer_id = houmer_id,
        search_date = search_date,
        places = places
    )
    return response


@app.get("/high_speed_moments/houmer/{houmer_id}/date/{search_date}/limit/{speed_limit}")
async def high_speed_moments(houmer_id: UUID, search_date: date, speed_limit: int, db: Session = Depends(get_db)):
    logger.info(f"Search high speed moments at {search_date} by houmerId: {houmer_id}")
    moments = HighSpeedService().get_high_speed_moments(db, houmer_id, search_date, speed_limit)
    
    response = HighSpeedMomentResponseDto(
        houmer_id = houmer_id,
        search_date = search_date,
        speed_limit = speed_limit,
        moments = moments
    )
    return response


@app.get("/property/{id}")
async def get_property(id: UUID, db: Session = Depends(get_db)):
    return PropertyService().get_property(db, id)


@app.post("/property/")
async def save_property(property_dto: PropertyDto, db: Session = Depends(get_db)):
    return PropertyService().save_property(db, property_dto)
