from __future__ import absolute_import, annotations

import uuid
from typing import Optional, Any

from smartplaces.models.base_class import BaseClass
from smartplaces.models.coordinates import Coordinates


class Place(BaseClass):
    """
    The model of a place of interest
    """

    TYPE_KEY = "type"
    NAME_KEY = "name"
    COORDINATES_KEY = "coordinates"

    def __init__(self, place_id: str, place_type: str, place_name: str, place_coordinates: Coordinates) -> None:
        """
        :param place_id: the id of the place of interest
        :param place_type: the type of place
        :param place_name: the name of the place of interest
        :param place_coordinates: the coordinates of the place of interest
        """

        self._place_id: str = place_id
        self._place_type: str = place_type
        self._place_name: str = place_name
        self._place_coordinates: Coordinates = place_coordinates

    def update(self, o: Place) -> Place:
        self._place_type = o._place_type
        self._place_name = o._place_name
        self._place_coordinates = o._place_coordinates
        return self

    def get_id(self) -> str:
        return self._place_id

    def get_field(self, field_key: str) -> Optional[Any]:
        if field_key == self.ID_KEY:
            return self.get_id()
        if field_key == self.TYPE_KEY:
            return self._place_type
        if field_key == self.NAME_KEY:
            return self._place_name
        if field_key == self.COORDINATES_KEY:
            return self._place_coordinates
        return None

    def to_repr(self) -> dict:
        return {
            self.ID_KEY: self._place_id,
            self.TYPE_KEY: self._place_type,
            self.NAME_KEY: self._place_name,
            self.COORDINATES_KEY: self._place_coordinates.to_repr()
        }

    @staticmethod
    def from_repr(raw_place: dict) -> Place:
        return Place(
            raw_place[Place.ID_KEY] if Place.ID_KEY in raw_place else str(uuid.uuid4()),
            raw_place[Place.TYPE_KEY], raw_place[Place.NAME_KEY],
            Coordinates.from_repr(raw_place[Place.COORDINATES_KEY])
        )

    def __eq__(self, o: Place) -> bool:
        return self._place_id == o._place_id and self._place_type == o._place_type and \
               self._place_name == o._place_name and self._place_coordinates == o._place_coordinates
