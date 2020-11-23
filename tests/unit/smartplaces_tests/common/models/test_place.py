from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.common.models.coordinates import Coordinates
from smartplaces.common.models.place import Place


class TestPlace(TestCase):

    def test_repr(self):
        place = Place("place_id", "place_type", "place_name", Coordinates(0.0, 0.0))
        self.assertEqual(place, Place.from_repr(place.to_repr()))
