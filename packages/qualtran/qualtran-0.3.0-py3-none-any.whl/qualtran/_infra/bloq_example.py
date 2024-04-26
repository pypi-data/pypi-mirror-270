#  Copyright 2023 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import typing
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple, Type, Union

from attrs import field, frozen

from .bloq import Bloq


@frozen
class BloqExample:
    """An instantiation of a bloq and its metadata.

    In particular, this class wraps a callable that returns a bloq instantiation with
    explicit attribute values.

    Consider using the decorator `@bloq_example` to construct a `BloqExample` from a function.

    Args:
        func: The function that returns the bloq instantiation. Calling the `BloqExample` instance
            will call this function.
        name: A name for the bloq instantiation.
        bloq_cls: The `Bloq` class that this instantiation is an instance of.
        generalizer: Passed to `get_bloq_counts_graph` calls for bloq-counts equivalence checking.
    """

    _func: Callable[[], Bloq] = field(repr=False, hash=False)
    name: str
    bloq_cls: Type[Bloq]
    generalizer: Callable[[Bloq], Optional[Bloq]] = field(
        converter=lambda x: tuple(x) if isinstance(x, Sequence) else x, default=lambda x: x
    )

    def make(self) -> Bloq:
        """Make the bloq."""
        return self._func()

    def __call__(self) -> Bloq:
        """This class is callable: it will make the bloq.

        This makes the `bloq_example` decorator make sense: we wrap a function, so this
        callable should do the same thing when called.
        """
        return self.make()


def _name_from_func_name(func: Callable[[], Bloq]) -> str:
    """Use the name of the function as the `BloqExample.name` when using the decorator."""
    return func.__name__.lstrip('_')


def _bloq_cls_from_func_annotation(func: Callable[[], Bloq]) -> Type[Bloq]:
    """Use the function return type annotation as the `BloqExample.bloq_cls` with the decorator."""
    anno = func.__annotations__
    if 'return' not in anno:
        raise ValueError(f'{func} must have a return type annotation.')

    cls = anno['return']
    assert issubclass(cls, Bloq), cls
    return cls


@typing.overload
def bloq_example(_func: Callable[[], Bloq], **kwargs: Any) -> BloqExample:
    ...


@typing.overload
def bloq_example(
    _func: None, *, generalizer: Callable[[Bloq], Optional[Bloq]] = lambda x: x
) -> Callable[[Callable[[], Bloq]], BloqExample]:
    ...


def bloq_example(
    _func: Callable[[], Bloq] = None, *, generalizer: Callable[[Bloq], Optional[Bloq]] = lambda x: x
):
    """Decorator to turn a function into a `BloqExample`.

    This will set `name` to the name of the function and `bloq_cls` according to the return-type
    annotation. You can also call the decorator with keyword arguments, which will be passed
    through to the `BloqExample` constructor.
    """

    def _inner(func: Callable[[], Bloq]) -> BloqExample:
        return BloqExample(
            func=func,
            name=_name_from_func_name(func),
            bloq_cls=_bloq_cls_from_func_annotation(func),
            generalizer=generalizer,
        )

    if _func is None:
        # Decorator called with arguments
        return _inner

    return _inner(_func)


def _to_tuple(T: Type):
    def _t(x: Iterable[T]) -> Tuple[T, ...]:
        return tuple(x)

    return _t


@frozen(kw_only=True)
class BloqDocSpec:
    """A collection of bloq examples and specifications for documenting a bloq class.

    This collects all the metadata and examples for a given bloq class. It is used to
    configure automatic documentation generation. The autogenerated notebooks currently
    contain the following sections:

     1. The bloq class's documentation. We render `bloq_cls`'s docstring to a markdown
        cell.
     2. Example instance construction. We use the `examples` to render code cells that
        construct the examples for use by further sections.
     3. Graphical signature. We display the bloq in a graphical form. This is prior to
        decomposition, so it shows the bloq's name and input/output registers i.e. its signature.
     4. Call graph. We display one of the example's call graph.

    Args:
        bloq_cls: The class we're documenting.
        import_line: How to import the bloq.
        examples: An iterable of `BloqExample` to use as example instances in the notebook.
        call_graph_example: The example to use to show the call graph, or `None` to omit a call
            graph. Note that this example must be included in `examples`.
    """

    bloq_cls: Type[Bloq]
    examples: Sequence[BloqExample] = field(converter=_to_tuple(BloqExample), factory=tuple)
    import_line: str = field()
    call_graph_example: Union[BloqExample, None] = field()

    @import_line.default
    def _import_line_default(self) -> str:
        pkg = '.'.join(self.bloq_cls.__module__.split('.')[:-1])
        line = f'from {pkg} import {self.bloq_cls.__name__}'
        return line

    @call_graph_example.default
    def _call_graph_example_default(self) -> Union[BloqExample, None]:
        if not self.examples:
            return None
        return self.examples[0]
