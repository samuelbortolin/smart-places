from __future__ import absolute_import, annotations

from typing import List

from flask import request
from flask_restful import Resource

from smartplaces.daos.collector import DaoCollector
from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.place import Place
from smartplaces.models.sensor import Sensor


class ResourcesBuilder:
    """
    The class for building the resources of the web service
    """

    @staticmethod
    def routes(dao_collector: DaoCollector):
        return [
            (PlaceResource, "/place", (dao_collector,)),
            (SensorResource, "/sensor", (dao_collector,)),
            (PlaceSensorsResource, "/place/sensor", (dao_collector,))
        ]


class PlaceResource(Resource):
    """
    The Resource for the management of the places of interest
    """

    PLACE_ID_KEY = "place_id"

    def __init__(self, dao_collector: DaoCollector):
        self._dao_collector = dao_collector

    def post(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400
        except Exception:
            return {"message": "Internal server error: could not parse posted data"}, 500

        try:
            self._dao_collector.place_dao.save_place(place)
        except Exception:
            return {"message": "Internal server error: could not save the place"}, 500

        return {"id": place.get_id()}, 201

    def get(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        try:
            place: Place = self._dao_collector.place_dao.get_place(place_id)
        except DaoEntryNotFound:
            return {"message": f"Place with id {place_id} not found"}, 404
        except Exception:
            return {"message": "Internal server error: could not get the place"}, 500

        return place.to_repr()

    def put(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400
        except Exception:
            return {"message": "Internal server error: could not parse posted data"}, 500

        try:
            self._dao_collector.place_dao.update_place(place)
        except Exception:
            return {"message": "Internal server error: could not update the place"}, 500

        return {}

    def delete(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        try:
            self._dao_collector.place_dao.delete_place(place_id)
        except Exception:
            return {"message": "Internal server error: could not delete the place"}, 500

        return {}


class SensorResource(Resource):
    """
    The Resource for the management of sensors
    """

    SENSOR_ID_KEY = "sensor_id"

    def __init__(self, dao_collector: DaoCollector):
        self._dao_collector = dao_collector

    def post(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            sensor: Sensor = Sensor.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400
        except Exception:
            return {"message": "Internal server error: could not parse posted data"}, 500

        try:
            self._dao_collector.sensor_dao.save_sensor(sensor)
        except Exception:
            return {"message": "Internal server error: could not save the sensor"}, 500

        return {"id": sensor.get_id()}, 201

    def get(self):
        sensor_id: str = request.args.get(self.SENSOR_ID_KEY)
        if not sensor_id:
            return {"message": f"Malformed request: missing required {self.SENSOR_ID_KEY} parameter"}, 400

        try:
            sensor: Sensor = self._dao_collector.sensor_dao.get_sensor(sensor_id)
        except DaoEntryNotFound:
            return {"message": f"Place with id {sensor_id} not found"}, 404
        except Exception:
            return {"message": "Internal server error: could not get the sensor"}, 500

        return sensor.to_repr()

    def put(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Malformed request: data is missing"}, 400

        try:
            sensor: Sensor = Sensor.from_repr(posted_data)
        except KeyError:
            return {"message": "Malformed request: could not parse posted data"}, 400
        except Exception:
            return {"message": "Internal server error: could not parse posted data"}, 500

        try:
            self._dao_collector.sensor_dao.update_sensor(sensor)
        except Exception:
            return {"message": "Internal server error: could not update the sensor"}, 500

        return {}

    def delete(self):
        sensor_id: str = request.args.get(self.SENSOR_ID_KEY)
        if not sensor_id:
            return {"message": f"Malformed request: missing required {self.SENSOR_ID_KEY} parameter"}, 400

        try:
            self._dao_collector.sensor_dao.delete_sensor(sensor_id)
        except Exception:
            return {"message": "Internal server error: could not delete the sensor"}, 500

        return {}


class PlaceSensorsResource(Resource):
    """
    The Resource for the getting the sensors present in a place
    """

    PLACE_ID_KEY = "place_id"

    def __init__(self, dao_collector: DaoCollector):
        self._dao_collector = dao_collector

    def get(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": f"Malformed request: missing required {self.PLACE_ID_KEY} parameter"}, 400

        try:
            self._dao_collector.place_dao.get_place(place_id)
            sensors: List[Sensor] = self._dao_collector.sensor_dao.search_place_sensors(place_id)
        except DaoEntryNotFound:
            return {"message": f"Place with id {place_id} not found"}, 404
        except Exception:
            return {"message": "Internal server error: could not get the place sensors"}, 500

        return [sensor.to_repr() for sensor in sensors]
