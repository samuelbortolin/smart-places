from __future__ import absolute_import, annotations

from smartplaces.common.models.coordinates import Coordinates


class Place:
    """
    The model of a place of interest
    """

    ID_KEY = "id"
    TYPE_KEY = "type"
    NAME_KEY = "name"
    COORDINATES_KEY = "coordinates"

    def __init__(self, place_id: str, place_type: str, place_name: str, place_coordinates: Coordinates) -> None:
        self.place_id: str = place_id
        self.place_type: str = place_type
        self.place_name: str = place_name
        self.place_coordinates: Coordinates = place_coordinates

    def update(self, o: Place) -> None:
        self.place_id = o.place_id
        self.place_type = o.place_type
        self.place_name = o.place_name
        self.place_coordinates = o.place_coordinates

    def to_repr(self) -> dict:
        return {
            self.ID_KEY: self.place_id,
            self.TYPE_KEY: self.place_type,
            self.NAME_KEY: self.place_name,
            self.COORDINATES_KEY: self.place_coordinates.to_repr()
        }

    @staticmethod
    def from_repr(raw_place: dict) -> Place:
        return Place(raw_place[Place.ID_KEY], raw_place[Place.TYPE_KEY], raw_place[Place.NAME_KEY],
                     raw_place[Place.COORDINATES_KEY].from_repr())

    def __eq__(self, o: Place) -> bool:
        return self.place_id == o.place_id and self.place_type == o.place_type and self.place_name == o.place_name \
               and self.place_coordinates == o.place_coordinates
