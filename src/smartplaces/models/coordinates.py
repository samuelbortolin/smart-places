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
        :param lat: the latitude of the place
        :param lon: the longitude of the place
        """

        self._lat: float = lat
        self._lon: float = lon

    @property
    def value(self) -> Dict[str: float, str: float]:
        return {
            self.LAT_KEY: self._lat,
            self.LON_KEY: self._lon
        }

    def to_repr(self) -> Dict[str: float, str: float]:
        return self.value

    @staticmethod
    def from_repr(raw_coordinates: dict) -> Coordinates:
        return Coordinates(raw_coordinates[Coordinates.LAT_KEY], raw_coordinates[Coordinates.LON_KEY])

    def __eq__(self, coordinates: Coordinates) -> bool:
        return self._lat == coordinates._lat and self._lon == coordinates._lon and self.value == coordinates.value
