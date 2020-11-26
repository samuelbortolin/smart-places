from __future__ import absolute_import, annotations

from smartplaces.models.coordinates import Coordinates
from smartplaces.models.place import Place
from smartplaces.models.sensor import Sensor
from tests.unit.smartplaces_tests.ws.common.common_test_ws import CommonWsTestCase


class TestPlaceSensorsResource(CommonWsTestCase):

    def test_get_place_sensors(self):
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })

        sensor = Sensor.from_repr({
            Sensor.ID_KEY: "id",
            Sensor.TYPE_KEY: "type",
            Sensor.PLACE_ID_KEY: "place_id"
        })

        place_id = "id"
