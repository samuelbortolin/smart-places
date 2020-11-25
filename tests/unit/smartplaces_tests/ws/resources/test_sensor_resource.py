from __future__ import absolute_import, annotations

from smartplaces.models.sensor import Sensor
from tests.unit.smartplaces_tests.ws.common.common_test_ws import CommonWsTestCase


class TestSensorResource(CommonWsTestCase):

    def test_post_sensor(self):
        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }

    def test_get_sensor(self):
        sensor = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })

        sensor_id = "id"

    def test_put_sensor(self):
        sensor_to_update = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })

        raw_sensor = {
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type2",
            Sensor.PLACE_ID_KEY: "place_id2"
        }

    def test_delete_sensor(self):
        sensor = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })

        sensor_id = "id"
