from abc import ABC

from interfaces.iorm_db import IORMethods


class SQLAlchemy(IORMethods):

    async def get(self, **kwargs):
        pass

    async def create(self, **kwargs):
        pass

    async def bulk_create(self, **kwargs):
        pass

    async def update(self, **kwargs):
        pass

    async def bulk_update(self, **kwargs):
        pass

    async def delete(self, **kwargs):
        pass

    async def bulk_delete(self, **kwargs):
        pass
