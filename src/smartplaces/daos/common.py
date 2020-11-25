from __future__ import absolute_import, annotations

from smartplaces.db.handler import DbHandler


class DaoEntryNotFound(Exception):
    pass


class SmartPlacesDao:
    """
    A base dao for storing the smart-places data
    """

    def __init__(self, db_handler: DbHandler, index: str) -> None:
        """
        :param db_handler: an handler for the database
        :param index: the index where to store the data
        """

        self._db_handler = db_handler
        self._index = index
        self._create_index(self._index)

    def _create_index(self, index_name: str) -> None:
        self._db_handler.create_index(index_name)
