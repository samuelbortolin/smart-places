from __future__ import absolute_import, annotations

import abc
from typing import Optional, List, Any


class DbHandler(abc.ABC):
    """
    A generic database handler
    """

    @abc.abstractmethod
    def create_index(self, index_name: str) -> None:
        """
        Create an index
        :param index_name: the name of the index to create
        """

        pass

    @abc.abstractmethod
    def add(self, object_id: str, object_repr: dict, index_name: str) -> None:
        """
        Add a representation of an object
        :param object_id: the id identifying the object
        :param object_repr: the representation of an object to add
        :param index_name: the name of the index where add
        """

        pass

    @abc.abstractmethod
    def get(self, object_id: str, index_name: str) -> Optional[dict]:
        """
        Get the representation of an object from an id
        :param object_id: the id identifying the object
        :param index_name: the name of the index where search the document into
        :return: the representation of the object with the requested id if found
        """

        pass

    @abc.abstractmethod
    def delete(self, object_id: str, index_name: str) -> None:
        """
        Delete the representation of an object from an id
        :param object_id: the id identifying the object
        :param index_name: the name of the index where search the document into
        """

        pass

    @abc.abstractmethod
    def search(self, field_key: str, field_value: Any, index_name: str) -> List[dict]:
        """
        Search entries satisfying a field_key with a field_value
        :param field_key: the key where to search
        :param field_value: the value to search
        :param index_name: the name of the index where search the document into
        :return: a list with the representation of the objects satisfying the field_key with the field_value
        """

        pass
