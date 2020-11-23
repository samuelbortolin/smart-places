from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.common.models.sensor import Sensor


class TestSensor(TestCase):

    def test_repr(self):
        sensor = Sensor("sensor_id", "sensor_type")
        self.assertEqual(sensor, Sensor.from_repr(sensor.to_repr()))
