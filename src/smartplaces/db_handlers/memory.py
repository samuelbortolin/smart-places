from __future__ import absolute_import, annotations

from typing import Optional, List, Any

from smartplaces.db_handlers.common import DbHandler


class MemoryHandler(DbHandler):
    """
    An handler to save the data in memory
    """

    def __init__(self) -> None:
        """
        Initialize an empty dictionary
        """

        self.data = {}

    def create_index(self, index_name: str) -> None:
        self.data[index_name] = {}

    def add(self, object_id: dict, object_repr: dict, index_name: str) -> None:
        self.data[index_name][object_id] = object_repr

    def get(self, object_id: str, index_name: str) -> Optional[dict]:
        return self.data[index_name][object_id] if object_id in self.data[index_name] else None

    def delete(self, object_id: str, index_name: str) -> None:
        self.data[index_name].pop(object_id, None)

    def search(self, field_key: str, field_value: Any, index_name: str) -> List[dict]:
        list_to_return = []
        for object_repr in self.data[index_name].values():
            if object_repr[field_key] == field_value:
                list_to_return.append(object_repr)
        return list_to_return
