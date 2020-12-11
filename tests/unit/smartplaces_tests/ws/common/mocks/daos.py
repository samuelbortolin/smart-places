from __future__ import absolute_import, annotations

from typing import List

from smartplaces.daos.collector import DaoCollector
from smartplaces.daos.place import PlaceDao
from smartplaces.daos.sensor import SensorDao
from smartplaces.models.place import Place
from smartplaces.models.sensor import Sensor


class MockPlaceDao(PlaceDao):
    """
    A mock for the place dao
    """

    def save_place(self, place: Place) -> None:
        pass

    def get_place(self, place_id: str) -> Place:
        pass

    def update_place(self, place: Place) -> None:
        pass

    def delete_place(self, place_id: str) -> None:
        pass


class MockSensorDao(SensorDao):
    """
    A mock for the sensor dao
    """

    def save_sensor(self, sensor: Sensor) -> None:
        pass

    def get_sensor(self, sensor_id: str) -> Sensor:
        pass

    def update_sensor(self, sensor: Sensor) -> None:
        pass

    def delete_sensor(self, sensor_id: str) -> None:
        pass

    def search_place_sensors(self, place_id: str) -> List[Sensor]:
        pass


class MockDaoCollectorBuilder:
    """
    The class for building the smart-places dao mocks
    """

    @staticmethod
    def build_mock_daos() -> DaoCollector:
        return DaoCollector(
            MockPlaceDao(),
            MockSensorDao()
        )
