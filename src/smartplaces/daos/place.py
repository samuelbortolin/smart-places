from __future__ import absolute_import, annotations

from typing import Optional

from smartplaces.daos.common import SmartPlacesDao, DaoEntryNotFound
from smartplaces.db.handler import DbHandler
from smartplaces.models.place import Place


class PlaceDao(SmartPlacesDao):
    """
    A base dao for storing the places data
    """

    INDEX = "smart-places_place"

    def __init__(self, db_handler: DbHandler):
        """
        :param db_handler: an handler for the database
        """

        super().__init__(db_handler, self.INDEX)

    def add(self, place: Place) -> None:
        """
        Store a place
        :param place: the place to store
        """

        self._db_handler.add(place.get_id(), place.to_repr(), self.INDEX)

    def get(self, place_id: str) -> Place:
        """
        Get a place from an id
        :param place_id: the id identifying the place
        :return: the place with the requested id
        :exception DaoEntryNotFound: raised if the place with the requested id is not found
        """

        place_repr: Optional[dict] = self._db_handler.get(place_id, self.INDEX)
        if place_repr:
            return Place.from_repr(place_repr)
        else:
            raise DaoEntryNotFound("Place not found for id [%s]" % place_id)

    def put(self, place: Place) -> None:
        """
        Update a place if present, if not create one
        :param place: the place to update
        """

        try:
            place_to_update = self.get(place.get_id())
            place_to_update.update(place)
        except DaoEntryNotFound:
            place_to_update = place
        self.add(place_to_update)

    def delete(self, place_id: str) -> None:
        self._db_handler.delete(place_id, self.INDEX)
