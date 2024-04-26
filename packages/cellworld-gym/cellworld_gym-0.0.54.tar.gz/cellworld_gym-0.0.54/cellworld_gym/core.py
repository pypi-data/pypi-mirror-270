import typing
from enum import Enum


class Observation(typing.List[float]):
    fields = []  # list of field names in the observation

    def __init__(self):
        super().__init__()
        for index, field in enumerate(self.__class__.fields):
            self.append(0.0)
            self._create_property(index=index,
                                  field=field)
        self.field_enum = Enum("fields", {field: index for index, field in enumerate(self.__class__.fields)})

    def _create_property(self,
                         index: int,
                         field: str):
        def getter(self):
            return self[index]

        def setter(self, value):
            self[index] = value

        setattr(self.__class__, field, property(getter, setter))

    def __setitem__(self, field: typing.Union[Enum, int], value):
        if isinstance(field, Enum):
            list.__setitem__(self, field.value, value)
        else:
            list.__setitem__(self, field, value)

    def __getitem__(self, field: typing.Union[Enum, int]) -> float:
        if isinstance(field, Enum):
            return list.__getitem__(self, field.value)
        else:
            return list.__getitem__(self, field)