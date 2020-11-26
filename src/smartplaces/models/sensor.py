from __future__ import absolute_import, annotations

import uuid


class Sensor:
    """
    The model of a sensor that collects a certain type of data and is in one place
    """

    ID_KEY = "id"
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

    def update(self, sensor: Sensor) -> Sensor:
        self._sensor_type = sensor._sensor_type
        self._place_id = sensor._place_id
        return self

    def get_id(self) -> str:
        return self._sensor_id

    def get_type(self) -> str:
        return self._sensor_type

    def get_place_id(self) -> str:
        return self._place_id

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

    def __eq__(self, sensor: Sensor) -> bool:
        return self._sensor_id == sensor._sensor_id and self._sensor_type == sensor._sensor_type and \
               self._place_id == sensor._place_id
