from __future__ import absolute_import, annotations


class Sensor:
    """
    The model of a sensor
    """

    ID_KEY = "id"
    TYPE_KEY = "type"

    def __init__(self, sensor_id: str, sensor_type: str) -> None:
        self.sensor_id: str = sensor_id
        self.sensor_type: str = sensor_type

    # each sensor associated to a place or a place with a list of sensors or both

    def to_repr(self) -> dict:
        return {
            self.ID_KEY: self.sensor_id,
            self.TYPE_KEY: self.sensor_type
        }

    @staticmethod
    def from_repr(raw_place: dict) -> Sensor:
        return Sensor(raw_place[Sensor.ID_KEY], raw_place[Sensor.TYPE_KEY])

    def __eq__(self, o: Sensor) -> bool:
        return self.sensor_id == o.sensor_id and self.sensor_type == o.sensor_type
