from abc import ABC
from interfaces.interface_service_mixins import ICreateMixin, IUpdateMixin, IDeleteMixin


class CreateMixin(ABC, ICreateMixin):

    def create(self, **kwargs) -> None:
        data = self.before_create(**kwargs)
        self.orm_model.create(**data)
        self.after_created(**data)

    def bulk_create(self, **kwargs) -> None:
        data = self.before_bulk_create(**kwargs)
        self.orm_model.bulk_create(**data)
        self.after_created(**data)

    @staticmethod
    def before_create(**kwargs):
        return kwargs

    @staticmethod
    def after_created(**kwargs):
        pass

    @staticmethod
    def before_bulk_create(**kwargs):
        return kwargs


class UpdateMixin(IUpdateMixin):
    def update(self, partial: bool = False, **kwargs):
        pass

    def bulk_update(self, partial: bool = False, **kwargs):
        pass

    @staticmethod
    def before_update(**kwargs):
        return kwargs

    @staticmethod
    def after_update(**kwargs):
        pass

    @staticmethod
    def before_bulk_update(**kwargs):
        return kwargs

    @staticmethod
    def after_bulk_update(**kwargs):
        pass


class DeleteMixin(IDeleteMixin):

    def delete(self, soft: bool = True, **kwargs):
        data = self.before_delete(**kwargs)
        if soft:
            data.update({"is_delete": True})
            self.orm_model.update(**data)
        else:
            self.orm_model.delete(**data)
        self.after_delete(**data)

    def bulk_delete(self, soft: bool = True, **kwargs):
        data = self.before_delete(**kwargs)
        if soft:
            data.update({"rife": {"is_delete": True}})
            self.orm_model.bulk_update(**data)
        else:
            self.orm_model.bulk_delete(**data)
        self.after_delete(**data)

    @staticmethod
    def before_delete(**kwargs):
        return kwargs

    @staticmethod
    def after_delete(**kwargs):
        pass

    @staticmethod
    def before_bulk_delete(**kwargs):
        return kwargs

    @staticmethod
    def after_bulk_delete(**kwargs):
        pass
