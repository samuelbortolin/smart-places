from __future__ import absolute_import, annotations

import abc
from typing import Optional, List, Any

from smartplaces.models.base_object import BaseObject


class DbHandler(abc.ABC):

    @abc.abstractmethod
    def create_index(self, index_name: str) -> None:
        pass

    @abc.abstractmethod
    def put(self, o: BaseObject, index_name: str) -> None:
        pass

    @abc.abstractmethod
    def get(self, object_id: str, index_name: str) -> Optional[BaseObject]:
        pass

    @abc.abstractmethod
    def delete(self, object_id: str, index_name: str) -> None:
        pass

    @abc.abstractmethod
    def search(self, field_key: str, field_value: Any, index_name: str) -> List[BaseObject]:
        pass


class MemoryHandler(DbHandler):

    def __init__(self) -> None:
        self.data = {}

    def create_index(self, index_name: str) -> None:
        self.data[index_name] = []

    def put(self, o: BaseObject, index_name: str) -> None:
        self.data[index_name].append(o)

    def get(self, object_id: str, index_name: str) -> Optional[BaseObject]:
        for o in self.data[index_name]:
            if o.get_id() == object_id:
                return o
        return None

    def delete(self, object_id: str, index_name: str) -> None:
        for o in self.data[index_name]:
            if o.get_id() == object_id:
                self.data[index_name].remove(o)

    def search(self, field_key: str, field_value: Any, index_name: str) -> List[BaseObject]:
        list_to_return = []
        for o in self.data[index_name]:
            if o.get_field(field_key) == field_value:
                list_to_return.append(o)
        return list_to_return
