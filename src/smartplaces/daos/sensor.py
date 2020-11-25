from __future__ import absolute_import, annotations

from typing import List, Optional

from smartplaces.daos.common import SmartPlacesDao, DaoEntryNotFound
from smartplaces.db_handlers.common import DbHandler
from smartplaces.models.sensor import Sensor


class SensorDao(SmartPlacesDao):
    """
    A dao for the management of the sensors data
    """

    INDEX = "smart-places_sensor"

    def __init__(self, db_handler: DbHandler):
        """
        :param db_handler: an handler for the database
        """

        super().__init__(db_handler, self.INDEX)

    def add(self, sensor: Sensor) -> None:
        """
        Store a sensor
        :param sensor: the sensor to store
        """

        self._db_handler.add(sensor.get_id(), sensor.to_repr(), self.INDEX)

    def get(self, sensor_id: str) -> Sensor:
        """
        Get a sensor from an id
        :param sensor_id: the id identifying the sensor
        :return: the sensor with the requested id
        :exception DaoEntryNotFound: raised if the sensor with the requested id is not found
        """

        sensor_repr: Optional[dict] = self._db_handler.get(sensor_id, self.INDEX)
        if sensor_repr:
            return Sensor.from_repr(sensor_repr)
        else:
            raise DaoEntryNotFound("Sensor not found for id [%s]" % sensor_id)

    def put(self, sensor: Sensor) -> None:
        """
        Update a sensor if present, if not create one
        :param sensor: the sensor to update
        """

        try:
            sensor_to_update = self.get(sensor.get_id())
            sensor_to_update.update(sensor)
        except DaoEntryNotFound:
            sensor_to_update = sensor
        self.add(sensor_to_update)

    def delete(self, sensor_id: str) -> None:
        self._db_handler.delete(sensor_id, self.INDEX)

    def search_sensors_in_place(self, place_id: str) -> List[Sensor]:
        sensors_repr: List[dict] = self._db_handler.search(Sensor.PLACE_ID_KEY, place_id, self.INDEX)
        sensors = [Sensor.from_repr(sensor_repr) for sensor_repr in sensors_repr]
        return sensors
