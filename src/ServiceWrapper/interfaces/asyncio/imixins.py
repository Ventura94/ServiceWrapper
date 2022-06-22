from abc import abstractmethod

from ServiceWrapper.interfaces.iservice import IService


class ICreateMixin(IService):
    @abstractmethod
    async def create(self, **kwargs):
        pass

    @abstractmethod
    async def bulk_create(self, **kwargs):
        pass

    @abstractmethod
    async def before_create(self, **kwargs):
        pass

    @abstractmethod
    async def after_created(self, **kwargs):
        pass

    @abstractmethod
    async def before_bulk_create(self, **kwargs):
        pass

    @abstractmethod
    async def after_bulk_created(self, **kwargs):
        pass


class IUpdateMixin(IService):
    @abstractmethod
    async def update(self, partial: bool = False, **kwargs):
        pass

    @abstractmethod
    async def bulk_update(self, partial: bool = False, **kwargs):
        pass

    @abstractmethod
    async def before_update(self, **kwargs):
        pass

    @abstractmethod
    async def after_update(self, **kwargs):
        pass

    @abstractmethod
    async def before_bulk_update(self, **kwargs):
        pass

    @abstractmethod
    async def after_bulk_update(self, **kwargs):
        pass


class IDeleteMixin(IService):
    @abstractmethod
    async def delete(self, soft: bool = True, **kwargs):
        pass

    @abstractmethod
    async def bulk_delete(self, soft: bool = True, **kwargs):
        pass

    @abstractmethod
    async def before_delete(self, **kwargs):
        pass

    @abstractmethod
    async def after_delete(self, **kwargs):
        pass

    @abstractmethod
    async def before_bulk_delete(self, **kwargs):
        pass

    @abstractmethod
    async def after_bulk_delete(self, **kwargs):
        pass
