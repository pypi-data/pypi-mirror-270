from __future__ import annotations
from typing import Callable, Protocol, Tuple, overload
from pythonix.internals import trail
from pythonix.internals.trail import Trail, Log
from functools import singledispatch


class HasInner[T](Protocol):

    inner: T


class Bind[T]:
    """
    Container that allows sequential functions calls to change its inner value and type.
    Transformations can be done with with either the `run` or `__call__` methods.
    #### Example
    ```python
    y: bool = (
        Bind(5)
        (lambda x: x + 6)   # -> 5 + 6 = 11
        (lambda x: x == 11) # -> 11 == 11 == True
    )
    assert y == True
    ```
    #### Methods
    - `run(Fn(T) -> U) -> Bind<U>`: Runs the provided function and returns a new `Bind` object containing
    its result
    - `__call__(Fn(T) -> U) -> Bind<U>`: Identical to the `run` function.
    """

    inner: T

    def __init__(self, inner: T) -> None:
        self.inner = inner

    def run[U](self, using: Callable[[T], U]) -> Bind[U]:
        """
        Performs a transformation on the contained value using the function provided.
        Returns a new `Bind` object containing the new value. Works only with single arity
        functions.
        """
        return Bind(using(self.inner))

    def __call__[U](self, using: Callable[[T], U]) -> Bind[U]:
        """
        Performs a transformation on the contained value using the function provided.
        Returns a new `Bind` object containing the new value. Works only with single arity
        functions.
        """
        return Bind(using(self.inner))


class Do[T]:
    """
    Container used to run arbitrary functions on an `inner` value without changing its
    state. Useful for logging, printing, or other inconsequential side effects.
    #### Example
    ```python
    do: Do[int] = Do(5)
    (
        do
        (print)             # Prints 5
        (lambda x: x * 2)   # -> 10
        (lambda x: x - 3)   # -> 2
    )
    assert do.inner == 5
    ```
    #### Methods
    - `run(Fn(T) -> U) -> Do[T]`: Runs the provided function on the contained value and returns itself.
    - `__call__(Fn(T) -> U) -> Do[T]`: Identical to the `run` function.
    """

    inner: T

    def __init__(self, inner: T) -> None:
        self.inner = inner

    def run[U](self, using: Callable[[T], U]) -> Do[T]:
        """
        Performs the provided function on the `inner` value, but does not return its result.
        Returns itself instead.
        """
        using(self.inner)
        return self

    def __call__[U](self, using: Callable[[T], U]) -> Do[T]:
        """
        Performs the provided function on the `inner` value, but does not return its result.
        Returns itself instead.
        """
        return self.run(using)


class Blaze[T]:
    """
    `Bind` container used to accumulate log messages during runtime without
    side effects to the functions being ran. Runs functions with an optional
    log message attached. If the function being called returns a `Trail` log container,
    then it will attach its logs to the currently accumulated logs.
    """

    logs: Tuple[Log, ...] = tuple()
    inner: trail.Trail[T]

    def __init__(self, inner: T | Trail[T], *logs: Log):
        match inner:
            case Trail():
                self.inner = inner
                self.logs = logs + inner.logs
            case _:
                self.inner = trail.new()(inner)
                self.logs = logs

    @overload
    def __call__[
        U
    ](self, using: Callable[[T], trail.Trail[U]], *logs: Log) -> Blaze[U]: ...

    @overload
    def __call__[U](self, using: Callable[[T], U], *logs: Log) -> Blaze[U]: ...

    def __call__[
        U
    ](self, using: Callable[[T], trail.Trail[U] | U], *logs: Log) -> Blaze[U]:
        """
        Call the function and attach the logs from the function `Trail` and the optional logs
        to the new instance of `Blaze` containing the result.
        """
        return Blaze(using(self.inner.inner), *(self.logs + logs))
