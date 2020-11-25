from __future__ import absolute_import, annotations

from smartplaces.daos.place import PlaceDao
from smartplaces.daos.sensor import SensorDao
from smartplaces.db.handler import DbHandler


class DaoCollector:
    """
    A collector of daos
    """

    def __init__(self, place_dao: PlaceDao, sensor_dao: SensorDao) -> None:
        """
        :param place_dao: a dao for storing the places
        :param sensor_dao: a dao for storing the sensors
        """

        self.place_dao = place_dao
        self.sensor_dao = sensor_dao

    @staticmethod
    def build(db_handler: DbHandler) -> DaoCollector:
        return DaoCollector(
            PlaceDao(db_handler),
            SensorDao(db_handler)
        )
