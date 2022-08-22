from app.schemas import HighSpeedMoment
from app.db.repositories import (
    get_locations_by_houmer_and_date
    )

class HighSpeedService():
    
    def get_high_speed_moments(self, db, houmer_id, search_date, speed_limit):
        moments = []
        location_history = get_locations_by_houmer_and_date(db, houmer_id, search_date)
        for position in location_history:
            if position.speed >= speed_limit:
                print(position)
                moment = HighSpeedMoment(
                    timestamp = position.timestamp,
                    speed = position.speed,
                    app_location_id = position.id
                )
                moments.append(moment)
        
        return moments