from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.models.sensor import Sensor


class TestSensor(TestCase):

    def test_repr(self):
        sensor = Sensor("id", "type", "place_id")
        self.assertEqual(sensor, Sensor.from_repr(sensor.to_repr()))

        raw_sensor = {
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        }
        self.assertIsInstance(Sensor.from_repr(raw_sensor), Sensor)

    def test_update(self):
        sensor = Sensor("id", "type", "place_id")
        sensor_updated = Sensor("id", "type", "place_id_2")
        self.assertEqual(sensor_updated, sensor.update(sensor_updated))

    def test_get_id(self):
        sensor = Sensor("id", "type", "place_id")
        self.assertEqual("id", sensor.get_id())

    def test_get_field(self):
        sensor = Sensor("id", "type", "place_id")
        self.assertEqual("id", sensor.get_field(Sensor.ID_KEY))
        self.assertEqual("type", sensor.get_field(Sensor.TYPE_KEY))
        self.assertEqual("place_id", sensor.get_field(Sensor.PLACE_ID_KEY))
