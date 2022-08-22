# README

## Description
This module is a python backend rest app, which intend to implement several requirements focused on storing and processing geolocated data sent from a mobile app.

### Software Requirements
- capture geolocation data
- obtain visited places report filtered by user (Houmer) and date
- obtain speed moments report filtered by user, date and limit

### Asumptions
- It is possible to get basic gps data from mobile phone app: latitude, longitude, speed, timestamp.
- Api security is implemented on higher layers such as api gateway tokens.


### Stack
- Python 3.10
- Postgres 12
- Docker to run as containered app

## Run code
The easyest way to run this code can be using 'docker-compose'.

`$ docker-compose up`

To check istalled containers:

`$ docker ps`

To stop containers using 'ctrl+C'.

## Load sample data
Once app is running it is recomended load sample data to play with it.

`$ PGPASSWORD='postgres' psql -h localhost -U postgres -p 5432 -d rest-app-back -f db_local.sample.sql`

## Endpoints documentation
You can check all endpoints that are implemented using swagger doc url:

`http://localhost:8080/docs`

## Manual Testing

* Send a houmer location:

```
POST   http://localhost:8080/app/location/
example BODY:
{
	"houmer_id": "52401e7d-5b4d-403a-9226-bbbbca3c7a65",
	"latitude": -33.443926234460804,
	"longitude": -70.61969725192385,
	"speed": 0,
	"timestamp": "2022-08-22T12:00:00.000-04:00"
}
```

* Visited places report
```
GET  http://localhost:8080/visited_places/houmer/6a49a709-bb24-4180-8aab-30d57f1a3518/date/2022-08-17
example response:
{
	"houmerId": "6a49a709-bb24-4180-8aab-30d57f1a3518",
	"searchDate": "2022-08-17",
	"places": [
		{
			"propertyId": "872c5420-dc90-43e4-80af-1891009aa868",
			"latitude": -33.44593132,
			"longitude": -70.62449161,
			"duration": 30
		},
		{
			"propertyId": "c8d38d6e-bfc4-4b33-850a-265d78098729",
			"latitude": -33.44614482,
			"longitude": -70.62860226,
			"duration": 24
		}
	]
}
```

* High speed moments report
```
GET  http://localhost:8070/high_speed_moments/houmer/:houmer_id/date/:search_date/limit/:speed_limit
example response:
{
	"houmerId": "6a49a709-bb24-4180-8aab-30d57f1a3518",
	"searchDate": "2022-08-17",
	"speedLimit": 7,
	"moments": [
		{
			"timestamp": "2022-08-17T11:54:00",
			"speed": 9,
			"appLocationId": "9ddef45a-05ef-4bfb-88f1-54f60cdc11c2"
		},
		{
			"timestamp": "2022-08-17T11:57:00",
			"speed": 8,
			"appLocationId": "58d5e376-cab2-4fb8-8251-411e390e6665"
		}
	]
}
```
