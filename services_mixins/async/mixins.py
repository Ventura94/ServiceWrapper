from interfaces.interface_service_mixins import ICreateMixin, IUpdateMixin, IDeleteMixin


class CreateMixin(ICreateMixin):

    async def create(self, **kwargs) -> None:
        data = await self.before_create(**kwargs)
        await self.orm_model.create(**data)
        await self.after_created(**data)

    async def bulk_create(self, **kwargs) -> None:
        data = await self.before_bulk_create(**kwargs)
        await self.orm_model.bulk_create(**data)
        await self.after_bulk_created(**data)

    @staticmethod
    async def before_create(**kwargs):
        return kwargs

    @staticmethod
    async def after_created(**kwargs):
        pass

    @staticmethod
    async def before_bulk_create(**kwargs):
        return kwargs

    @staticmethod
    async def after_bulk_created(**kwargs):
        pass


class UpdateMixin(IUpdateMixin):
    async def update(self, partial: bool = False, **kwargs):
        pass

    async def bulk_update(self, partial: bool = False, **kwargs):
        pass

    @staticmethod
    async def before_update(**kwargs):
        return kwargs

    @staticmethod
    async def after_update(**kwargs):
        pass

    @staticmethod
    async def before_bulk_update(**kwargs):
        return kwargs

    @staticmethod
    async def after_bulk_update(**kwargs):
        pass


class DeleteMixin(IDeleteMixin):

    async def delete(self, soft: bool = True, **kwargs):
        data = await self.before_delete(**kwargs)
        if soft:
            data.update({"is_delete": True})
            await self.orm_model.update(**data)
        else:
            await self.orm_model.delete(**data)
        await self.after_delete(**data)

    async def bulk_delete(self, soft: bool = True, **kwargs):
        data = await self.before_delete(**kwargs)
        if soft:
            data.update({"rife": {"is_delete": True}})
            await self.orm_model.bulk_update(**data)
        else:
            await self.orm_model.bulk_delete(**data)
        await self.after_delete(**data)

    @staticmethod
    async def before_delete(**kwargs):
        return kwargs

    @staticmethod
    async def after_delete(**kwargs):
        pass

    @staticmethod
    async def before_bulk_delete(**kwargs):
        return kwargs

    @staticmethod
    async def after_bulk_delete(**kwargs):
        pass
