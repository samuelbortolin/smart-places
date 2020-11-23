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
        :param sensor_id: The id of the sensor
        :param sensor_type: The type of data that the sensor collects
        :param place_id: The id of the place where is the sensor
        """

        self.sensor_id: str = sensor_id
        self.sensor_type: str = sensor_type
        self.place_id: str = place_id

    def update(self, o: Sensor) -> Sensor:
        self.place_id = o.place_id
        return self

    def to_repr(self) -> dict:
        return {
            self.ID_KEY: self.sensor_id,
            self.TYPE_KEY: self.sensor_type,
            self.PLACE_ID_KEY: self.place_id
        }

    @staticmethod
    def from_repr(raw_sensor: dict) -> Sensor:
        return Sensor(
            raw_sensor[Sensor.ID_KEY] if Sensor.ID_KEY in raw_sensor else str(uuid.uuid4()),
            raw_sensor[Sensor.TYPE_KEY],
            raw_sensor[Sensor.PLACE_ID_KEY]
        )

    def __eq__(self, o: Sensor) -> bool:
        return self.sensor_id == o.sensor_id and self.sensor_type == o.sensor_type and self.place_id == o.place_id
