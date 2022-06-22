from abc import ABC, abstractmethod
from typing import Union

from ServiceWrapper.interfaces.sync.iorm_db import IORMethods as AsyncORM
from ServiceWrapper.interfaces.asyncio.iorm_db import IORMethods as SyncORM


class IService(ABC):
    @property
    @abstractmethod
    def orm_model(self) -> Union[AsyncORM, SyncORM]:
        ...
