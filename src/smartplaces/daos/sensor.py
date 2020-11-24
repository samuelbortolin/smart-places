from __future__ import absolute_import, annotations

from typing import List, Optional

from smartplaces.daos.common import SmartPlacesDao, DaoEntryNotFound
from smartplaces.db.handler import DbHandler
from smartplaces.models.sensor import Sensor


class SensorDao(SmartPlacesDao):

    INDEX = "smart-places_sensor"

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler, self.INDEX)

    def put(self, sensor: Sensor) -> None:
        self._db_handler.put(sensor, self.INDEX)

    def get(self, sensor_id: str) -> Sensor:
        sensor: Optional[Sensor] = self._db_handler.get(sensor_id, self.INDEX)
        if sensor is None:
            raise DaoEntryNotFound("Sensor not found for id [%s]" % sensor_id)
        else:
            return sensor

    def delete(self, sensor_id: str) -> None:
        self._db_handler.delete(sensor_id, self.INDEX)

    def search(self, place_id: str) -> List[Sensor]:
        sensors: List[Sensor] = self._db_handler.search(Sensor.PLACE_ID_KEY, place_id, self.INDEX)
        return sensors
