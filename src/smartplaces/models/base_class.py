from __future__ import absolute_import, annotations

import abc
from typing import Optional, Any


class BaseClass(abc.ABC):
    """
    The base class model, every object must have an unique identifier that in the representation
    has to be the value related to the key `ID_KEY`
    """

    ID_KEY = "id"

    @abc.abstractmethod
    def get_id(self) -> str:
        pass

    @abc.abstractmethod
    def get_field(self, field_key: str) -> Optional[Any]:
        pass

    @abc.abstractmethod
    def to_repr(self) -> dict:
        pass

    @staticmethod
    @abc.abstractmethod
    def from_repr(raw_data: dict) -> BaseClass:
        pass
