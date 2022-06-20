from abc import ABC, abstractmethod
from interfaces.iorm_db import IORMethods


class IService(ABC):

    @property
    @abstractmethod
    def orm_model(self) -> IORMethods:
        ...


class ICreateMixin(IService):

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def bulk_create(self, **kwargs):
        pass

    @abstractmethod
    def before_create(self, **kwargs):
        pass

    @abstractmethod
    def after_created(self, **kwargs):
        pass

    @abstractmethod
    def before_bulk_create(self, **kwargs):
        pass

    @abstractmethod
    def after_bulk_created(self, **kwargs):
        pass


class IUpdateMixin(IService):

    @abstractmethod
    def update(self, partial: bool = False, **kwargs):
        pass

    @abstractmethod
    def bulk_update(self, partial: bool = False, **kwargs):
        pass

    @abstractmethod
    def before_update(self, **kwargs):
        pass

    @abstractmethod
    def after_update(self, **kwargs):
        pass

    @abstractmethod
    def before_bulk_update(self, **kwargs):
        pass

    @abstractmethod
    def after_bulk_update(self, **kwargs):
        pass


class IDeleteMixin(IService):

    @abstractmethod
    def delete(self, soft: bool = True, **kwargs):
        pass

    @abstractmethod
    def bulk_delete(self, soft: bool = True, **kwargs):
        pass

    @abstractmethod
    def before_delete(self, **kwargs):
        pass

    @abstractmethod
    def after_delete(self, **kwargs):
        pass

    @abstractmethod
    def before_bulk_delete(self, **kwargs):
        pass

    @abstractmethod
    def after_bulk_delete(self, **kwargs):
        pass
