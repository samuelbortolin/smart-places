from __future__ import absolute_import, annotations

from typing import Dict


class Coordinates:
    """
    The model of the coordinates of a place
    """

    LAT_KEY = "lat"
    LON_KEY = "lon"

    def __init__(self, lat: float, lon: float) -> None:
        """
        :param lat: The latitude of the place
        :param lon: The longitude of the place
        """

        self.lat: float = lat
        self.lon: float = lon

    @property
    def value(self) -> Dict[str: float, str: float]:
        return {
            self.LAT_KEY: self.lat,
            self.LON_KEY: self.lon
        }

    def to_repr(self) -> Dict[str: float, str: float]:
        return self.value

    @staticmethod
    def from_repr(raw_coordinates: dict) -> Coordinates:
        return Coordinates(raw_coordinates[Coordinates.LAT_KEY], raw_coordinates[Coordinates.LON_KEY])

    def __eq__(self, o: Coordinates) -> bool:
        return self.lat == o.lat and self.lon == o.lon and self.value == o.value
