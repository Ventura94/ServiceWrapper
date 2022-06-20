from ServiceWrapper.interfaces.interface_service_mixins import ICreateMixin, IUpdateMixin, IDeleteMixin


class CreateMixin(ICreateMixin):
    @classmethod
    async def create(cls, **kwargs) -> None:
        data = await cls.before_create(**kwargs)
        await cls.orm_model.create(**data)
        await cls.after_created(**data)

    @classmethod
    async def bulk_create(cls, **kwargs) -> None:
        data = await cls.before_bulk_create(**kwargs)
        await cls.orm_model.bulk_create(**data)
        await cls.after_bulk_created(**data)

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
    @classmethod
    async def update(cls, partial: bool = False, **kwargs):
        pass

    @classmethod
    async def bulk_update(cls, partial: bool = False, **kwargs):
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

    @classmethod
    async def delete(cls, soft: bool = True, **kwargs):
        data = await cls.before_delete(**kwargs)
        if soft:
            data.update({"is_delete": True})
            await cls.orm_model.update(**data)
        else:
            await cls.orm_model.delete(**data)
        await cls.after_delete(**data)

    @classmethod
    async def bulk_delete(cls, soft: bool = True, **kwargs):
        data = await cls.before_delete(**kwargs)
        if soft:
            data.update({"rife": {"is_delete": True}})
            await cls.orm_model.bulk_update(**data)
        else:
            await cls.orm_model.bulk_delete(**data)
        await cls.after_delete(**data)

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
