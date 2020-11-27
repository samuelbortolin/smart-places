from __future__ import absolute_import, annotations

import json

from mock import Mock

from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.coordinates import Coordinates
from smartplaces.models.place import Place
from smartplaces.ws.resources import PlaceResource
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
        self.dao_collector.place_dao.save_place = Mock(return_value=None)
        response = self.client.post("/place", json=raw_place)

        self.assertEqual(201, response.status_code)
        self.assertEqual({"id": "id"}, json.loads(response.data))

    def test_post_place_missing_data(self):
        raw_place = {
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }
        self.dao_collector.place_dao.save_place = Mock(return_value=None)
        response = self.client.post("/place", json=None)

        self.assertEqual(400, response.status_code)
        self.assertEqual({"message": "Malformed request: data is missing"}, json.loads(response.data))

    def test_post_place_without_id(self):
        raw_place = {
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }
        self.dao_collector.place_dao.save_place = Mock(return_value=None)
        response = self.client.post("/place", json=raw_place)

        self.assertEqual(201, response.status_code)

    def test_post_place_malformed_request(self):
        raw_place = {
            Place.ID_KEY: "id",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }
        self.dao_collector.place_dao.save_place = Mock(return_value=None)
        response = self.client.post("/place", json=raw_place)

        self.assertEqual(400, response.status_code)
        self.assertEqual({"message": "Malformed request: could not parse posted data"}, json.loads(response.data))

    def test_post_place_exception(self):
        raw_place = {
            Place.ID_KEY: "id",
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }
        self.dao_collector.place_dao.save_place = Mock(side_effect=Exception)
        response = self.client.post("/place", json=raw_place)

        self.assertEqual(500, response.status_code)
        self.assertEqual({"message": "Internal server error: could not save the place"}, json.loads(response.data))

    def test_get_place(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: place_id,
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        self.dao_collector.place_dao.get_place = Mock(return_value=place)
        response = self.client.get(f"/place?{PlaceResource.PLACE_ID_KEY}={place_id}")

        self.assertEqual(200, response.status_code)
        self.assertEqual(place.to_repr(), json.loads(response.data))

    def test_get_place_missing_parameter(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: place_id,
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        self.dao_collector.place_dao.get_place = Mock(return_value=place)
        response = self.client.get("/place")

        self.assertEqual(400, response.status_code)
        self.assertEqual({"message": f"Malformed request: missing required {PlaceResource.PLACE_ID_KEY} parameter"}, json.loads(response.data))

    def test_get_place_not_found(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: place_id,
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        self.dao_collector.place_dao.get_place = Mock(side_effect=DaoEntryNotFound)
        response = self.client.get(f"/place?{PlaceResource.PLACE_ID_KEY}={place_id}")

        self.assertEqual(404, response.status_code)
        self.assertEqual({"message": f"Place with id {place_id} not found"}, json.loads(response.data))

    def test_get_place_exception(self):
        place_id = "id"
        place = Place.from_repr({
            Place.ID_KEY: place_id,
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        })
        self.dao_collector.place_dao.get_place = Mock(side_effect=Exception)
        response = self.client.get(f"/place?{PlaceResource.PLACE_ID_KEY}={place_id}")

        self.assertEqual(500, response.status_code)
        self.assertEqual({"message": "Internal server error: could not get the place"}, json.loads(response.data))

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
