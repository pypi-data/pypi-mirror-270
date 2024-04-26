from typing import NamedTuple, Tuple, Callable, ParamSpec
from datetime import datetime, timezone
from abc import ABCMeta
from enum import Enum

P = ParamSpec("P")


class Log(NamedTuple):
    datetime: datetime
    message: str

    def __str__(self) -> str:
        return f'{self.__class__.__name__}("{self.datetime.strftime('%Y-%m-%dT%H:%M:%SZ')}", "{self.message}")'

class Info(Log):
    ...

class Debug(Log):
    ...

class Warning(Log):
    ...

class Error(Log):
    ...

class Critical(Log):
    ...


def log[L: (Log)](log_type: type[L]):
    """
    Creates a new `Log` instance with the specified message attached
    """
    def inner(message: str) -> L:
        """
        Attach a message to the log 
        """
        return log_type(datetime.now(timezone.utc), message)

    return inner


debug = log(Debug)
info = log(Info)
warning = log(Warning)
error = log(Error)
critical = log(Critical)


class Trail[T](NamedTuple):
    """
    Container type used to wrap a value with a series of `Log` type records
    """
    logs: Tuple[Log, ...]
    inner: T


def new[L: (Log)](*logs: L):
    """
    Create a new `Trail` object with the desired logs attached.
    """
    def get_inner[T](inner: T) -> Trail[T]:
        """
        Attach the wrapped value to the `Trail`
        """
        return Trail(logs, inner)

    return get_inner


def append[L: (Log)](*logs: L):
    """
    Append a new series of logs to a `Trail`
    """
    def inner[T](trail: Trail[T]) -> Trail[T]:

        return new(*(trail.logs + logs))(trail.inner)

    return inner


def logs[T, L: (Log)](trail: Trail[T]) -> Tuple[L, ...]:
    """
    Convenience function to return the logs of a `Trail`
    """
    return trail.logs


def trail[L: (Log)](*logs: L):
    """
    Decorator function used to wrap the output of a function with a default set of logs.
    This also changes the output of the function to return a `Trail` of the type returned
    by the function.
    """
    def inner[U](func: Callable[P, U]):

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Trail[U]:

            return new(*logs)(func(*args, **kwargs))

        return wrapper

    return inner

