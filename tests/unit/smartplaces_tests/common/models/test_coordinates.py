from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.common.models.coordinates import Coordinates


class TestCoordinates(TestCase):

    def test_repr(self):
        coordinates = Coordinates(0.0, 0.0)
        self.assertEqual(coordinates, Coordinates.from_repr(coordinates.to_repr()))
