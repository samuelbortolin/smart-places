from __future__ import absolute_import, annotations

from flask import request
from flask_restful import Resource

from smartplaces.common.models.place import Place
from smartplaces.common.models.sensor import Sensor


class ResourcesBuilder:

    @staticmethod
    def routes():
        return [
            (PlaceResource, '/place', ()),
            (SensorResource, '/sensor', ()),
            (SensorsInPlaceResource, '/place/sensor', ())
        ]


class PlaceResource(Resource):
    """
    The Resource for the management of the places of interest
    """

    PLACE_ID_KEY = "place_id"

    def get(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        # return the place with the place_id equal to the one requested or 404 place not found

    def post(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400

        # create a new place

    def put(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400

        # update a place

    def delete(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        # delete the place with the place_id equal to the one requested


class SensorResource(Resource):
    """
    The Resource for the management of sensors
    """

    SENSOR_ID_KEY = "sensor_id"

    def get(self):
        sensor_id: str = request.args.get(self.SENSOR_ID_KEY)
        if not sensor_id:
            return {"message": f"Malformed request: missing required {self.SENSOR_ID_KEY} parameter"}, 400

        # return the sensor with the sensor_id equal to the one requested or 404 sensor not found

    def post(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            sensor: Sensor = Sensor.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400

        # create a new sensor

    def put(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            sensor: Sensor = Sensor.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400

        # update a sensor

    def delete(self):
        sensor_id: str = request.args.get(self.SENSOR_ID_KEY)
        if not sensor_id:
            return {"message": f"Malformed request: missing required {self.SENSOR_ID_KEY} parameter"}, 400

        # delete the sensor with the sensor_id equal to the one requested


class SensorsInPlaceResource(Resource):
    """
    The Resource for the getting the sensors present in a place
    """

    PLACE_ID_KEY = "place_id"

    def get(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        # return the sensors in the place with the place_id equal to the one requested or 404 place not found
