from dataclasses import Field, dataclass, field, fields
from typing import Callable, Self, Type, TypeVar

T = TypeVar("T")
F = TypeVar("F")


LAZY_LOAD_TYPE = Callable[[], T] | T


@dataclass(slots=True)
class Fields:
    class_type: Type
    class_fields: dict[str, Field] = field(init=False)

    def __post_init__(self):
        self.class_fields = dict(map(lambda x: (x.name, x), fields(self.class_type)))

    def __getattr__(self, item: str) -> Field:
        try:
            return self.class_fields[item]
        except KeyError:
            raise AttributeError(item)

    def __getitem__(self, item: str) -> Field:
        try:
            return self.class_fields[item]
        except KeyError:
            raise AttributeError(item)


class ClassPropertyDescriptor(object):
    def __init__(
        self,
        get_: classmethod | None,
        set_: classmethod | None = None,
    ):
        self.get_ = get_
        self.set_ = set_

    def __get__(
        self,
        obj: Type[T] | None,
        klass: Type[T] | None = None,
    ) -> F:
        if klass is None:
            klass = type(obj)

        func = self.get_.__get__(obj, klass)

        return func()

    def __set__(self, obj: Type[T] | None, value: F) -> None:
        if not self.set_:
            raise AttributeError("can't set attribute")

        type_ = type(obj)
        func = self.set_.__get__(obj, type_)

        return func(value)

    def setter(
        self,
        func: Callable[[Type[T], F], None] | classmethod,
    ) -> Self:
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)

        self.set_ = func

        return self


def classproperty(
    func: Callable[[Type[T]], F] | classmethod
) -> ClassPropertyDescriptor:
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)


class Singleton(type):
    __instances__ = {}

    def __call__(cls, reset: bool = False, *args, **kwargs):
        if reset or cls not in cls.__instances__:
            cls.__instances__[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instances__.get(cls, None)

    @property
    def instance(cls) -> Self | None:
        return cls.__instances__.get(cls, None)

    def clear_instance(cls):
        try:
            del Singleton.__instances__[cls]
        except KeyError:
            pass


class Beholder(type):
    __inheritors__ = {}

    def __new__(mcs, name, bases, dct):
        klass = type.__new__(mcs, name, bases, dct)

        for base in klass.mro()[1:-1]:
            klass_name = mcs.__process__(klass.__name__)
            if base not in mcs.__inheritors__:
                mcs.__inheritors__[base] = {}
            mcs.__inheritors__[base][klass_name] = klass

        return klass

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    @staticmethod
    def __process__(name: str):
        return name.lower().replace("-", "_")

    @property
    def __modules__(cls):
        return cls.__inheritors__.get(cls, {})

    def get(cls, name: str, default: any = None):
        name = cls.__process__(name)
        return cls.__modules__.get(name, default)

    @classmethod
    def get_wrapper(mcs, cls) -> Callable[[str], Type[T] | None]:
        def _wrapper(name: str) -> Type[T] | None:
            return cls.get(name)

        return _wrapper
