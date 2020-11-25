from __future__ import absolute_import, annotations

from smartplaces.models.coordinates import Coordinates
from smartplaces.models.place import Place
from tests.unit.smartplaces_tests.ws.common.common_test_ws import CommonWsTestCase


class TestPlaceResource(CommonWsTestCase):

    def test_post_place(self):
        raw_place = {
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }

    def test_get_place(self):
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })

        place_id = "id"

    def test_put_place(self):
        place_to_update = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })

        raw_place = {
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type2",
            Place.NAME_KEY: "name2",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0750,
                Coordinates.LON_KEY: 11.1220
            }
        }

    def test_delete_place(self):
        place = Place.from_repr({
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })

        place_id = "id"
