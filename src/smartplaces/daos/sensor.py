from __future__ import absolute_import, annotations

import abc
from typing import List

from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.sensor import Sensor


class SensorDao(abc.ABC):
    """
    A basic dao for the management of sensors
    """

    @abc.abstractmethod
    def save_sensor(self, sensor: Sensor) -> None:
        """
        Save a sensor
        :param sensor: the sensor to save
        """

        pass

    @abc.abstractmethod
    def get_sensor(self, sensor_id: str) -> Sensor:
        """
        Get a sensor from an id
        :param sensor_id: the identifier of the sensor
        :return: the sensor with the requested id
        :exception DaoEntryNotFound: raised if the sensor with the requested id is not found
        """

        pass

    @abc.abstractmethod
    def update_sensor(self, sensor: Sensor) -> None:
        """
        Update a sensor if present, if not create one
        :param sensor: the sensor to update
        """

        pass

    @abc.abstractmethod
    def delete_sensor(self, sensor_id: str) -> None:
        """
        Delete a sensor from an id if present
        :param sensor_id: the identifier of the sensor
        """

        pass

    @abc.abstractmethod
    def search_place_sensors(self, place_id: str) -> List[Sensor]:
        """
        Search the sensors in a place from an id
        :param place_id: the identifier of the place
        """

        pass


class SensorMemoryDao(SensorDao):
    """
    A dao for the management of sensors in the memory
    """

    def __init__(self):
        """
        Initialize an empty dictionary
        """

        self._sensors = {}

    def save_sensor(self, sensor: Sensor) -> None:
        """
        Save a sensor
        :param sensor: the sensor to save
        """

        self._sensors[sensor.get_id()] = sensor

    def get_sensor(self, sensor_id: str) -> Sensor:
        """
        Get a sensor from an id
        :param sensor_id: the id identifying the sensor
        :return: the sensor with the requested id
        :exception DaoEntryNotFound: raised if the sensor with the requested id is not found
        """

        try:
            return self._sensors[sensor_id]
        except KeyError:
            raise DaoEntryNotFound("Sensor not found for id [%s]" % sensor_id)

    def update_sensor(self, sensor: Sensor) -> None:
        """
        Update a sensor if present, if not create one
        :param sensor: the sensor to update
        """

        try:
            sensor_to_update = self.get_sensor(sensor.get_id())
            sensor_to_update.update(sensor)
        except DaoEntryNotFound:
            sensor_to_update = sensor
        self.save_sensor(sensor_to_update)

    def delete_sensor(self, sensor_id: str) -> None:
        """
        Delete a sensor from an id if present
        :param sensor_id: the identifier of the sensor
        """

        self._sensors.pop(sensor_id, None)

    def search_place_sensors(self, place_id: str) -> List[Sensor]:
        """
        Search the sensors in a place from an id
        :param place_id: the identifier of the place
        """

        sensors = []
        for sensor in self._sensors.values():
            if sensor.get_place_id() == place_id:
                sensors.append(sensor)
        return sensors
