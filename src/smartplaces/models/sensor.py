from __future__ import absolute_import, annotations

import uuid
from typing import Optional, Any

from smartplaces.models.common import BaseClass


class Sensor(BaseClass):
    """
    The model of a sensor that collects a certain type of data and is in one place
    """

    TYPE_KEY = "type"
    PLACE_ID_KEY = "place_id"

    def __init__(self, sensor_id: str, sensor_type: str, place_id: str) -> None:
        """
        :param sensor_id: the id of the sensor
        :param sensor_type: the type of data that the sensor collects
        :param place_id: the id of the place where is the sensor
        """

        self._sensor_id: str = sensor_id
        self._sensor_type: str = sensor_type
        self._place_id: str = place_id

    def update(self, o: Sensor) -> Sensor:
        self._sensor_type = o._sensor_type
        self._place_id = o._place_id
        return self

    def get_id(self) -> str:
        return self._sensor_id

    def get_field(self, field_key: str) -> Optional[Any]:
        if field_key == self.ID_KEY:
            return self.get_id()
        if field_key == self.TYPE_KEY:
            return self._sensor_type
        if field_key == self.PLACE_ID_KEY:
            return self._place_id
        return None

    def to_repr(self) -> dict:
        return {
            self.ID_KEY: self._sensor_id,
            self.TYPE_KEY: self._sensor_type,
            self.PLACE_ID_KEY: self._place_id
        }

    @staticmethod
    def from_repr(raw_sensor: dict) -> Sensor:
        return Sensor(
            raw_sensor[Sensor.ID_KEY] if Sensor.ID_KEY in raw_sensor else str(uuid.uuid4()),
            raw_sensor[Sensor.TYPE_KEY],
            raw_sensor[Sensor.PLACE_ID_KEY]
        )

    def __eq__(self, o: Sensor) -> bool:
        return self._sensor_id == o._sensor_id and self._sensor_type == o._sensor_type and self._place_id == o._place_id
