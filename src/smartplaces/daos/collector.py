from __future__ import absolute_import, annotations

from smartplaces.daos.place import PlaceDao, PlaceMemoryDao
from smartplaces.daos.sensor import SensorDao, SensorMemoryDao


class DaoCollector:
    """
    A collector of daos for the management of data
    """

    def __init__(self, place_dao: PlaceDao, sensor_dao: SensorDao) -> None:
        """
        :param place_dao: a dao for the management of places
        :param sensor_dao: a dao for the management of sensors
        """

        self.place_dao = place_dao
        self.sensor_dao = sensor_dao

    @staticmethod
    def build_memory_daos() -> DaoCollector:
        return DaoCollector(
            PlaceMemoryDao(),
            SensorMemoryDao()
        )
