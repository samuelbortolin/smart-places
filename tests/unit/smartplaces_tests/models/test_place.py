from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.models.coordinates import Coordinates
from smartplaces.models.place import Place


class TestPlace(TestCase):

    def test_repr(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual(place, Place.from_repr(place.to_repr()))

        raw_place = {
            Place.TYPE_KEY: "type",
            Place.NAME_KEY: "name",
            Place.COORDINATES_KEY: {
                Coordinates.LAT_KEY: 46.0748,
                Coordinates.LON_KEY: 11.1217
            }
        }
        self.assertIsInstance(Place.from_repr(raw_place), Place)

    def test_update(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        place_updated = Place("id", "type2", "name2", Coordinates(46.0750, 11.1220))
        self.assertEqual(place_updated, place.update(place_updated))

    def test_get_id(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual("id", place.get_id())

    def test_get_type(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual("type", place.get_type())

    def test_get_name(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual("name", place.get_name())

    def test_get_coordinates(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual(Coordinates(46.0748, 11.1217), place.get_coordinates())
