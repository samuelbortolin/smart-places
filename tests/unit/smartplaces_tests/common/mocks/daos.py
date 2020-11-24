from __future__ import absolute_import, annotations

from smartplaces.daos.collector import DaoCollector
from smartplaces.daos.place import PlaceDao
from smartplaces.daos.sensor import SensorDao


class MockPlaceDao(PlaceDao):

    def __init__(self):
        super().__init__(None)

    def _create_index(self, index_name: str) -> None:
        pass


class MockSensorDao(SensorDao):

    def __init__(self):
        super().__init__(None)

    def _create_index(self, index_name: str) -> None:
        pass


class MockDaoBuilder:

    @staticmethod
    def build() -> DaoCollector:
        return DaoCollector(
            MockPlaceDao(),
            MockSensorDao()
        )
