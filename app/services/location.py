from app.db.repositories import save_app_location

class LocationService():

    def save(self, db, app_location_dto):
        app_location = save_app_location(db, app_location_dto)
        return app_location