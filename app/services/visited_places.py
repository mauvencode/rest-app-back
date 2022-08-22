from app.schemas import VisitedPlace
from app.db.repositories import (
    get_property_list, 
    get_locations_by_houmer_and_date
    )
from shapely.geometry import Point, Polygon
import ast


class VisitedPlacesService():

    def get_visited_places(self, db, houmer_id, search_date):
        property_list = get_property_list(db)
        location_history = get_locations_by_houmer_and_date(db, houmer_id, search_date)
        places_times = {}
        property_cache = {}

        for position in location_history:
            for property in property_list:
                if property.geofence != None:
                    property_geofence_points = ast.literal_eval(property.geofence)
                    property_location = Polygon(property_geofence_points)
                else:
                    property_location = Point(property.longitude, property.latitude).buffer(0.001)

                houmer_position = Point(position.longitude, position.latitude)
                is_property = property_location.contains(houmer_position)
                if is_property:
                    #print(f"{property.id} {position.timestamp}")
                    set_of_times = places_times.get(property.id)
                    if set_of_times == None:
                        new_set = set(())
                        new_set.add(position.timestamp)
                        places_times[property.id] = new_set
                    else:
                        set_of_times.add(position.timestamp)
                        places_times[property.id] = set_of_times

                    if property_cache.get(property.id) is None:
                        property_cache[property.id] = property

        #print(f"Places:")
        #print(places_times)

        places = []
        for place_key in places_times.keys():
            set_of_times = places_times.get(place_key)
            min_time = min(set_of_times)
            max_time = max(set_of_times)
            duration = max_time - min_time
            #print(f"{duration}")
            vp = VisitedPlace(
                property_id = place_key,
                duration = int(duration.seconds/60),
                longitude = property_cache.get(place_key).longitude,
                latitude = property_cache.get(place_key).latitude
            )
            places.append(vp)
        
        return places