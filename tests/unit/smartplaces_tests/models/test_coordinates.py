from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.models.coordinates import Coordinates


class TestCoordinates(TestCase):

    def test_repr(self):
        coordinates = Coordinates(46.0748, 11.1217)
        self.assertEqual(coordinates, Coordinates.from_repr(coordinates.to_repr()))

    def test_value(self):
        coordinates = Coordinates(46.0748, 11.1217)
        self.assertEqual({Coordinates.LAT_KEY: 46.0748, Coordinates.LON_KEY: 11.1217}, coordinates.value)
