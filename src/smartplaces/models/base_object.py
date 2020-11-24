from __future__ import absolute_import, annotations

import abc
from typing import Optional, Any


class BaseObject(abc.ABC):

    @abc.abstractmethod
    def get_id(self) -> str:
        pass

    @abc.abstractmethod
    def get_field(self, field_key: str) -> Optional[Any]:
        pass
