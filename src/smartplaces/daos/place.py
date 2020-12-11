from __future__ import absolute_import, annotations

import abc

from smartplaces.daos.common import DaoEntryNotFound
from smartplaces.models.place import Place


class PlaceDao(abc.ABC):
    """
    A basic dao for the management of places
    """

    @abc.abstractmethod
    def save_place(self, place: Place) -> None:
        """
        Save a place
        :param place: the place to save
        """

        pass

    @abc.abstractmethod
    def get_place(self, place_id: str) -> Place:
        """
        Get a place from an id
        :param place_id: the identifier of the place
        :return: the place with the requested id
        :exception DaoEntryNotFound: raised if the place with the requested id is not found
        """

        pass

    @abc.abstractmethod
    def update_place(self, place: Place) -> None:
        """
        Update a place if present, if not create one
        :param place: the place to update
        """

        pass

    @abc.abstractmethod
    def delete_place(self, place_id: str) -> None:
        """
        Delete a place from an id if present
        :param place_id: the identifier of the place
        """

        pass


class PlaceMemoryDao(PlaceDao):
    """
    A dao for the management of places in the memory
    """

    def __init__(self):
        """
        Initialize an empty dictionary
        """

        self._places = {}

    def save_place(self, place: Place) -> None:
        """
        Save a place
        :param place: the place to save
        """

        self._places[place.get_id()] = place

    def get_place(self, place_id: str) -> Place:
        """
        Get a place from an id
        :param place_id: the identifier of the place
        :return: the place with the requested id
        :exception DaoEntryNotFound: raised if the place with the requested id is not found
        """

        try:
            return self._places[place_id]
        except KeyError:
            raise DaoEntryNotFound("Place not found for id [%s]" % place_id)

    def update_place(self, place: Place) -> None:
        """
        Update a place if present, if not create one
        :param place: the place to update
        """

        try:
            place_to_update = self.get_place(place.get_id())
            place_to_update.update(place)
        except DaoEntryNotFound:
            place_to_update = place
        self.save_place(place_to_update)

    def delete_place(self, place_id: str) -> None:
        """
        Delete a place from an id if present
        :param place_id: the identifier of the place
        """

        self._places.pop(place_id, None)
