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
        place_updated = Place("id", "type2", "name2", Coordinates(46.0748, 11.1217))
        self.assertEqual(place_updated, place.update(place_updated))

    def test_get_id(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual("id", place.get_id())

    def test_get_field(self):
        place = Place("id", "type", "name", Coordinates(46.0748, 11.1217))
        self.assertEqual("id", place.get_field(Place.ID_KEY))
        self.assertEqual("type", place.get_field(Place.TYPE_KEY))
        self.assertEqual("name", place.get_field(Place.NAME_KEY))
        self.assertEqual(Coordinates(46.0748, 11.1217), place.get_field(Place.COORDINATES_KEY))
