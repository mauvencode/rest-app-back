from app.db.repositories import save_app_location

class LocationService():

    def save(self, db, app_location_dto):
        app_location = save_app_location(
            db, 
            app_location_dto.houmer_id,
            app_location_dto.latitude,
            app_location_dto.longitude,
            app_location_dto.speed,
            app_location_dto.timestamp
            )
        return app_location