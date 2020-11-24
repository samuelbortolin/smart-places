from __future__ import absolute_import, annotations

from typing import Optional

from smartplaces.daos.common import SmartPlacesDao, DaoEntryNotFound
from smartplaces.db.handler import DbHandler
from smartplaces.models.place import Place


class PlaceDao(SmartPlacesDao):

    INDEX = "smart-places_place"

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler, self.INDEX)

    def put(self, place: Place) -> None:
        self._db_handler.put(place, self.INDEX)

    def get(self, place_id: str) -> Place:
        place: Optional[Place] = self._db_handler.get(place_id, self.INDEX)
        if place is None:
            raise DaoEntryNotFound("Place not found for id [%s]" % place_id)
        else:
            return place

    def delete(self, place_id: str) -> None:
        self._db_handler.delete(place_id, self.INDEX)
