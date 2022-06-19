from interfaces.iorm_db import IORMethods


class MongoDB(IORMethods):
    async def get_current(self, query):
        return await self.model.find_one(query)

    async def get(self, **kwargs):
        return await self.model.find_one(kwargs)

    async def create(self, **kwargs) -> None:
        await self.model.insert_one(kwargs)

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
