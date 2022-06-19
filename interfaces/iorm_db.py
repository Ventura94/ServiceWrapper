from typing import Dict, Union
from decimal import Decimal
from abc import ABC, abstractmethod


class IORMethods(ABC):

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def get_current(self, query):
        pass

    @abstractmethod
    def get(self, **kwargs) -> Dict[str, Union[str, int, float, bool, Decimal]]:
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def bulk_create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def bulk_update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass

    @abstractmethod
    def bulk_delete(self, **kwargs):
        pass
