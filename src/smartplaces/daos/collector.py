from __future__ import absolute_import, annotations

from smartplaces.daos.place import PlaceDao
from smartplaces.daos.sensor import SensorDao
from smartplaces.db.handler import DbHandler


class DaoCollector:

    def __init__(self, place_dao: PlaceDao, sensor_dao: SensorDao) -> None:
        self.place_dao = place_dao
        self.sensor_dao = sensor_dao

    @staticmethod
    def build(db_handler: DbHandler) -> DaoCollector:
        return DaoCollector(
            PlaceDao(db_handler),
            SensorDao(db_handler)
        )
