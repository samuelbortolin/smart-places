from __future__ import absolute_import, annotations

import json

from mock import Mock

from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.coordinates import Coordinates
from smartplaces.models.place import Place
from smartplaces.models.sensor import Sensor
from smartplaces.ws.resources import PlaceSensorsResource
from tests.unit.smartplaces_tests.ws.common.common_test_ws import CommonWsTestCase


class TestPlaceSensorsResource(CommonWsTestCase):

    def test_get_place_sensors(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        sensors = [Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })]
        self.dao_collector.place_dao.get_place = Mock(return_value=place)
        self.dao_collector.sensor_dao.search_place_sensors = Mock(return_value=sensors)
        response = self.client.get(f"/place/sensor?{PlaceSensorsResource.PLACE_ID_KEY}={place_id}")
        self.assertEqual(200, response.status_code)
        self.assertEqual([sensor.to_repr() for sensor in sensors], json.loads(response.data))

    def test_get_place_sensors_missing_parameter(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        sensors = [Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })]
        self.dao_collector.place_dao.get_place = Mock(return_value=place)
        self.dao_collector.sensor_dao.search_place_sensors = Mock(return_value=sensors)
        response = self.client.get("/place/sensor")
        self.assertEqual(400, response.status_code)

    def test_get_place_sensors_not_found(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        sensors = [Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })]
        self.dao_collector.place_dao.get_place = Mock(side_effect=DaoEntryNotFound)
        self.dao_collector.sensor_dao.search_place_sensors = Mock(return_value=sensors)
        response = self.client.get(f"/place/sensor?{PlaceSensorsResource.PLACE_ID_KEY}={place_id}")
        self.assertEqual(404, response.status_code)

    def test_get_place_sensors_exception_place(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        sensors = [Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })]
        self.dao_collector.place_dao.get_place = Mock(side_effect=Exception)
        self.dao_collector.sensor_dao.search_place_sensors = Mock(return_value=sensors)
        response = self.client.get(f"/place/sensor?{PlaceSensorsResource.PLACE_ID_KEY}={place_id}")
        self.assertEqual(500, response.status_code)

    def test_get_place_sensors_exception_sensors(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        sensors = [Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })]
        self.dao_collector.place_dao.get_place = Mock(return_value=place)
        self.dao_collector.sensor_dao.search_place_sensors = Mock(side_effect=Exception)
        response = self.client.get(f"/place/sensor?{PlaceSensorsResource.PLACE_ID_KEY}={place_id}")
        self.assertEqual(500, response.status_code)
