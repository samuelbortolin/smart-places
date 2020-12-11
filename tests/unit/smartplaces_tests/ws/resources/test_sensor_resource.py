from __future__ import absolute_import, annotations

import json

from mock import Mock

from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.sensor import Sensor
from smartplaces.ws.resources import SensorResource
from tests.unit.smartplaces_tests.ws.common.common_test_ws import CommonWsTestCase


class TestSensorResource(CommonWsTestCase):

    def test_post_sensor(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.save_sensor = Mock(return_value=None)
        response = self.client.post("/sensor", json=raw_sensor)
        self.assertEqual(201, response.status_code)
        self.assertEqual({"id": "id"}, json.loads(response.data))

    def test_post_sensor_missing_data(self):
        self.dao_collector.sensor_dao.save_sensor = Mock(return_value=None)
        response = self.client.post("/sensor", json=None)
        self.assertEqual(400, response.status_code)

    def test_post_sensor_without_id(self):
        raw_sensor = {
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.save_sensor = Mock(return_value=None)
        response = self.client.post("/sensor", json=raw_sensor)
        self.assertEqual(201, response.status_code)

    def test_post_sensor_malformed_request(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.save_sensor = Mock(return_value=None)
        response = self.client.post("/sensor", json=raw_sensor)
        self.assertEqual(400, response.status_code)

    def test_post_sensor_exception(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.save_sensor = Mock(side_effect=Exception)
        response = self.client.post("/sensor", json=raw_sensor)
        self.assertEqual(500, response.status_code)

    def test_get_sensor(self):
        sensor_id = "id"
        sensor = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })
        self.dao_collector.sensor_dao.get_sensor = Mock(return_value=sensor)
        response = self.client.get(f"/sensor?{SensorResource.SENSOR_ID_KEY}={sensor_id}")
        self.assertEqual(200, response.status_code)
        self.assertEqual(sensor.to_repr(), json.loads(response.data))

    def test_get_sensor_missing_parameter(self):
        sensor = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })
        self.dao_collector.sensor_dao.get_sensor = Mock(return_value=sensor)
        response = self.client.get("/sensor")
        self.assertEqual(400, response.status_code)

    def test_get_sensor_not_found(self):
        sensor_id = "id"
        self.dao_collector.sensor_dao.get_sensor = Mock(side_effect=DaoEntryNotFound)
        response = self.client.get(f"/sensor?{SensorResource.SENSOR_ID_KEY}={sensor_id}")
        self.assertEqual(404, response.status_code)

    def test_get_sensor_exception(self):
        sensor_id = "id"
        self.dao_collector.sensor_dao.get_sensor = Mock(side_effect=Exception)
        response = self.client.get(f"/sensor?{SensorResource.SENSOR_ID_KEY}={sensor_id}")
        self.assertEqual(500, response.status_code)

    def test_put_sensor(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.update_sensor = Mock(return_value=None)
        response = self.client.put("/sensor", json=raw_sensor)
        self.assertEqual(200, response.status_code)
        self.assertEqual({}, json.loads(response.data))

    def test_put_sensor_missing_data(self):
        self.dao_collector.sensor_dao.update_sensor = Mock(return_value=None)
        response = self.client.put("/sensor", json=None)
        self.assertEqual(400, response.status_code)

    def test_put_sensor_without_id(self):
        raw_sensor = {
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.update_sensor = Mock(return_value=None)
        response = self.client.put("/sensor", json=raw_sensor)
        self.assertEqual(200, response.status_code)

    def test_put_sensor_malformed_request(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.update_sensor = Mock(return_value=None)
        response = self.client.put("/sensor", json=raw_sensor)
        self.assertEqual(400, response.status_code)

    def test_put_sensor_exception(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.dao_collector.sensor_dao.update_sensor = Mock(side_effect=Exception)
        response = self.client.put("/sensor", json=raw_sensor)
        self.assertEqual(500, response.status_code)

    def test_delete_sensor(self):
        sensor_id = "id"
        self.dao_collector.sensor_dao.delete_sensor = Mock(return_value=None)
        response = self.client.delete(f"/sensor?{SensorResource.SENSOR_ID_KEY}={sensor_id}")
        self.assertEqual(200, response.status_code)
        self.assertEqual({}, json.loads(response.data))

    def test_delete_place_missing_parameter(self):
        self.dao_collector.sensor_dao.delete_sensor = Mock(return_value=None)
        response = self.client.delete("/sensor")
        self.assertEqual(400, response.status_code)

    def test_delete_place_exception(self):
        sensor_id = "id"
        self.dao_collector.sensor_dao.delete_sensor = Mock(side_effect=Exception)
        response = self.client.delete(f"/sensor?{SensorResource.SENSOR_ID_KEY}={sensor_id}")
        self.assertEqual(500, response.status_code)
