import typing
from collections.abc import Callable

_py_type = type  # Alias for type where it is used as a name

__version__: str
INTERNALS_DICT: str

def get_fields(cls: type, *, local: bool = False) -> dict[str, Field]: ...

def get_flags(cls:type) -> dict[str, bool]: ...

def _get_inst_fields(inst: typing.Any) -> dict[str, typing.Any]: ...

class _NothingType:
    ...
NOTHING: _NothingType

# Stub Only
_codegen_type = Callable[[type], tuple[str, dict[str, typing.Any]]]

class MethodMaker:
    funcname: str
    code_generator: _codegen_type
    def __init__(self, funcname: str, code_generator: _codegen_type) -> None: ...
    def __repr__(self) -> str: ...
    def __get__(self, instance, cls) -> Callable: ...

def get_init_maker(
    null: _NothingType = NOTHING,
    extra_code: None | list[str] = None
) -> Callable[[type], tuple[str, dict[str, typing.Any]]]: ...

def init_maker(cls: type) -> tuple[str, dict[str, typing.Any]]: ...
def repr_maker(cls: type) -> tuple[str, dict[str, typing.Any]]: ...
def eq_maker(cls: type) -> tuple[str, dict[str, typing.Any]]: ...

def frozen_setattr_maker(cls: type) -> tuple[str, dict[str, typing.Any]]: ...

def frozen_delattr_maker(cls: type) -> tuple[str, dict[str, typing.Any]]: ...

init_desc: MethodMaker
repr_desc: MethodMaker
eq_desc: MethodMaker
frozen_setattr_desc: MethodMaker
frozen_delattr_desc: MethodMaker
default_methods: frozenset[MethodMaker]

_T = typing.TypeVar("_T")

@typing.overload
def builder(
    cls: type[_T],
    /,
    *,
    gatherer: Callable[[type], dict[str, Field]],
    methods: frozenset[MethodMaker] | set[MethodMaker],
    flags: dict[str, bool] | None = None,
) -> type[_T]: ...

@typing.overload
def builder(
    cls: None = None,
    /,
    *,
    gatherer: Callable[[type], dict[str, Field]],
    methods: frozenset[MethodMaker] | set[MethodMaker],
    flags: dict[str, bool] | None = None,
) -> Callable[[type[_T]], type[_T]]: ...


class Field:
    default: _NothingType | typing.Any
    default_factory: _NothingType | typing.Any
    type: _NothingType | _py_type
    doc: None | str

    __classbuilder_internals__: dict

    def __init__(
        self,
        *,
        default: _NothingType | typing.Any = NOTHING,
        default_factory: _NothingType | typing.Any = NOTHING,
        type: _NothingType | _py_type = NOTHING,
        doc: None | str = None,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Field | object) -> bool: ...
    def validate_field(self) -> None: ...
    @classmethod
    def from_field(cls, fld: Field, /, **kwargs: typing.Any) -> Field: ...


class SlotFields(dict):
    ...

def make_slot_gatherer(field_type: type[Field] = Field) -> Callable[[type], dict[str, Field]]: ...

def slot_gatherer(cls: type) -> dict[str, Field]:
    ...

def is_classvar(hint: object) -> bool: ...

def make_annotation_gatherer(
    field_type: type[Field] = Field,
    leave_default_values: bool = True,
) -> Callable[[type], dict[str, Field]]: ...

def annotation_gatherer(cls: type) -> dict[str, Field]: ...

def check_argument_order(cls: type) -> None: ...

@typing.overload
def slotclass(
    cls: type[_T],
    /,
    *,
    methods: frozenset[MethodMaker] | set[MethodMaker] = default_methods,
    syntax_check: bool = True
) -> type[_T]: ...

@typing.overload
def slotclass(
    cls: None = None,
    /,
    *,
    methods: frozenset[MethodMaker] | set[MethodMaker] = default_methods,
    syntax_check: bool = True
) -> Callable[[type[_T]], type[_T]]: ...

@typing.overload
def annotationclass(
    cls: type[_T],
    /,
    *,
    methods: frozenset[MethodMaker] | set[MethodMaker] = default_methods,
) -> type[_T]: ...

@typing.overload
def annotationclass(
        cls: None = None,
        /,
        *,
        methods: frozenset[MethodMaker] | set[MethodMaker] = default_methods,
) -> Callable[[type[_T]], type[_T]]: ...

@typing.overload
def fieldclass(cls: type[_T], /, *, frozen: bool = False) -> type[_T]: ...

@typing.overload
def fieldclass(cls: None = None, /, *, frozen: bool = False) -> Callable[[type[_T]], type[_T]]: ...
