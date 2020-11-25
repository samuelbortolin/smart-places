from __future__ import absolute_import, annotations

from smartplaces.daos.collector import DaoCollector
from smartplaces.daos.place import PlaceDao
from smartplaces.daos.sensor import SensorDao


class MockPlaceDao(PlaceDao):
    """
    A mock for the places dao
    """

    def __init__(self):
        super().__init__(None)

    def _create_index(self, index_name: str) -> None:
        pass


class MockSensorDao(SensorDao):
    """
    A mock for the sensor dao
    """

    def __init__(self):
        super().__init__(None)

    def _create_index(self, index_name: str) -> None:
        pass


class MockDaoBuilder:
    """
    The class for building the smart-places dao mocks
    """

    @staticmethod
    def build() -> DaoCollector:
        return DaoCollector(
            MockPlaceDao(),
            MockSensorDao()
        )
