"""
Functions used to operate over data structures
"""
from typing import Callable, Iterable, Iterator, Any, SupportsIndex
from functools import reduce
from pythonix.internals.res import null_and_error_safe


def filterx[T](using: Callable[[T], bool]) -> Callable[[Iterable[T]], Iterator[T]]:
    """
    Filter over an `Iterable` with a function that takes each of its elements and returns a True or False.
    True evaluations are kept while False are not kept in the result.
    """
    def get_data(iterable: Iterable[T]) -> filter[T]:

        return filter(using, iterable)

    return get_data


def mapx[T, U](using: Callable[[T], U]) -> Callable[[Iterable[T]], Iterator[U]]:
    """
    Run the `using` function over an `Iterable` and return an `Iterator` containing the result 
    """
    def get_data(iterable: Iterable[T]) -> map[U]:

        return map(using, iterable)

    return get_data


def reducex[
    S, T, U
](using: Callable[[S, T], U]) -> Callable[[Iterable[S | T]], Iterator[U]]:
    """
    Run a function that takes two arguments over an `Iterable` to produce a single result. 
    """
    def get_data(iterable: Iterable[S | T]) -> reduce[U]:

        return reduce(using, iterable)

    return get_data


def attr[U](name: str, type_hint: type[U] = Any):
    """
    Used to safely retrieve attributes from classes in a functional way.
    Can be used with a `type_hint` parameter to provide better type hint support.
    #### Example
    ```python
    from pythonix import Res
    from collections import namedtuple

    Point = namedtuple('Point', ('x', 'y'))
    p1 = Point(5, 4)
    x: Res[int, Nil] = attr('x', int)(p1)
    z: Res[int, Nil] = attr('z')(p1)

    assert x.inner = 5
    assert z.inner is Nil
    ```
    """

    @null_and_error_safe(AttributeError)
    def inner[T](obj: T) -> U:
        return getattr(obj, name)

    return inner


def item(index: SupportsIndex):
    """
    Used to safely retrieve items from sequences and mappings in a functional way.
    Can be used with a `type_hint` parameter to provide better type hint support.
    #### Example
    ```python
    from pythonix import Res

    p1 = (5, 4)
    x: Res[int, Nil] = item(0)(p1)
    z: Res[int, Nil] = item(2)(p1)

    assert x.inner = 5
    assert z.inner is Nil
    ```
    """

    @null_and_error_safe(IndexError, KeyError)
    def inner[T](iterable: Iterable[T]) -> T:
        return iterable[index]

    return inner
