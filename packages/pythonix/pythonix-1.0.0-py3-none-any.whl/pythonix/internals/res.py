from __future__ import annotations
from typing import TypeVar, Generic, NamedTuple, cast, ParamSpec, Callable
from pythonix.internals.types import Fn

P = ParamSpec("P")

E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")


class Nil(Exception):
    """
    Error class used to represent an unexpected `None` value.
    """

    def __init__(self, message: str = "Did not expect None"):
        super().__init__(message)


class Ok[T](NamedTuple):
    """
    Represents a successful outcome of a function that could have failed.
    Useful for pattern matching on a function that returns `Ok[T] | Err[E]`
    ### Example
    ```python
    success: Res[int, ValueError] = ok(5)(ValueError)
    match success:
        case Ok(t):
            assert t == 5
        case Err(e):
            raise e
    ```
    """

    inner: T


class Err(Generic[E], NamedTuple):
    """
    Represents a successful outcome of a function that could have failed.
    Useful for pattern matching on a function that returns `Ok[T] | Err[E]`
    ### Example
    ```python
    failure: Res[int, ValueError] = err(int)(ValueError("Failed to do a thing"))
    match failure:
        case Ok():
            ...
        case Err(e):
            raise e
    ```
    """

    inner: E


type Res[T, E] = Ok[T] | Err[E]


def err[T](ok_type: type[T]) -> Callable[[E], Res[T, E]]:
    """
    Sets the `Ok` type of the `Res`
    #### Example
    ```python
    failure: Res[int, ValueError] = err(int)(ValueError())
    ```
    """

    def get_err(exception_object: E) -> Res[T, E]:
        """
        Sets the value of the `Err` inner value of the `Res`
        """
        return Err(exception_object)

    return get_err


def ok[T](ok_obj: T) -> Callable[[type[E]], Res[T, E]]:
    """
    Sets the `Ok` inner value of the `Res`
    #### Example
    ```python
    success: Res[int, ValueError] = ok(5)(ValueError)
    ```
    """

    def get_err(err_type: type[E]) -> Res[T, E]:
        """
        Sets the `Err` type of the `Res`
        """
        return Ok(ok_obj)

    return get_err


def some[T](inner: T | None) -> Res[T, Nil]:
    """
    Converts the passed in value `T | None` to `Err[Nil]` if None,
    else `Ok[T]`. Useful for checking for null values before they
    cause unexpected defects.
    """
    if inner is not None:
        return ok(inner)(Nil)
    return err(T)(Nil())


def is_ok[T](res: Res[T, E]) -> bool:
    """
    Return `True` if the `Res` is `Ok`.
    """
    match res:
        case Ok():
            return True
        case Err():
            return False


def is_err[T](res: Res[T, E]) -> bool:
    """
    Return `True` if the `Res` is `Err`.
    """
    match res:
        case Ok():
            return False
        case Err():
            return True


def is_ok_and[T](predicate: Fn[T, bool]) -> Callable[[Res[T, E]], bool]:
    """
    Return `True` if the `Res` is `Ok` and the `predicate` evaluates to `True`.
    """
    def inner(res: Res[T, E]) -> bool:

        match res:
            case Ok(t):
                return predicate(t)
            case Err():
                return False

    return inner


def is_err_and[T](predicate: Fn[E, bool]) -> Callable[[Res[T, E]], bool]:
    """
    Return `True` if the `Res` is `Err` and the `predicate` evaluates to `True`
    """
    def inner(res: Res[T, E]) -> bool:

        match res:
            case Ok():
                return False
            case Err(e):
                return predicate(e)

    return inner


def unwrap[T](result: Res[T, E]) -> T:
    """
    Return the `Ok` value or panic if `Err`
    """
    match result:
        case Ok(value):
            return value
        case Err(e):
            raise e


def unwrap_or[T](default: T) -> Fn[Res[T, E], T]:
    """
    Return the `Ok` value if `Ok`, else return the default
    """
    def inner(res: Res[T, E]) -> T:

        match res:
            case Ok(val):
                return val
            case Err():
                return default

    return inner


def unwrap_or_else[T](on_err: Callable[[], T]) -> Fn[Res[T, E], T]:
    """
    Return the `Ok` value if `Ok`, else run the `on_err` function that returns the same type.
    """
    def inner(res: Res[T, E]) -> T:

        match res:
            case Ok(val):
                return val
            case Err():
                return on_err()

    return inner


UnwrapErr = ValueError("Attempted to retrieve an Err from an Ok")


def unwrap_err[T](result: Res[T, E]) -> E:
    """
    Return the `Err`, else panic if `Ok`
    """
    match result:
        case Ok():
            raise UnwrapErr
        case Err(e):
            return e


def map[T, U](using: Fn[T, U]) -> Fn[Res[T, E], Res[U, E]]:
    """
    Run the function on the `Ok` if `Ok`, else return the current `Err`
    """
    def inner(res: Res[T, E]) -> Res[U, E]:
        match res:
            case Ok(t):
                return ok(using(t))(E)
            case Err():
                return cast(Res[U, E], res)

    return inner


def map_or[T, U](using: Fn[T, U]) -> Callable[[U], Callable[[Res[T, E]], Res[U, E]]]:
    """
    Runs the function on the `Ok` or return the `default` if `Err`
    """
    def get_default(default: U) -> Callable[[Res[T, E]], Res[U, E]]:

        def inner(res: Res[T, E]) -> Res[U, E]:

            match res:
                case Ok(t):
                    return ok(using(t))(E)
                case Err():
                    return ok(default)(E)

        return inner

    return get_default


def map_catch[
    T, U
](using: Callable[[T], U]) -> Callable[[type[E]], Callable[[Res[T, E]], Res[U, E]]]:
    """
    Runs the function that could fail if `Ok`, else return the current `Err`
    """
    def get_catch(catch: type[E]) -> Callable[[Res[T, E]], Res[U, E]]:

        def inner(res: Res[T, E]) -> Res[U, E]:

            match res:
                case Ok(t):
                    try:
                        return ok(using(t))(E)
                    except catch as e:
                        return err(U)(e)
                case Err(e):
                    return cast(Res[U, E], res)

        return inner

    return get_catch


def map_or_else[
    T, U
](using: Fn[T, U]) -> Callable[[Callable[[], U]], Callable[[Res[T, E]], Res[U, E]]]:
    """
    Runs the provided function if `Ok`, or runs the default function if `Err`
    """
    def get_default(default: Callable[[], U]) -> Callable[[Res[T, E]], Res[U, E]]:

        def inner(res: Res[T, E]) -> Res[U, E]:

            match res:
                case Ok(t):
                    return ok(using(t))(E)
                case Err():
                    return ok(default())(E)

        return inner

    return get_default


def and_then[T, U](using: Fn[T, Res[U, E]]) -> Fn[Res[T, E], Res[U, E]]:
    """
    Runs the function that returns a new `Res` if `Ok`, else return the current `Err`
    """
    def inner(res: Res[T, E]) -> Res[U, E]:
        match res:
            case Ok(t):
                return cast(Res[U, E], using(t))
            case Err():
                return cast(Res[U, E], res)

    return inner


def or_else[T, U](using: Fn[E, Res[U, F]]) -> Fn[Res[T, E], Res[T, F]]:
    """
    Runs the function that returns a new `Res` if in `Err`, else it will return the current `Ok`
    """
    def inner(res: Res[T, E]) -> Res[T, F]:
        match res:
            case Ok():
                return cast(Res[T, F], res)
            case Err(e):
                return cast(Res[T, F], using(e))

    return inner


def and_then_catch[T, U](using: Fn[T, U]):
    """
    Runs the function that could fail, catching the specified error and returning a new `Res`.
    Will only be ran if `Ok`, else it will return its current `Err`
    """
    def get_catch(catch: type[F]) -> Fn[Res[T, E], Res[U, E | F]]:

        def inner(res: Res[T, E]) -> Res[U, E | F]:
            match res:
                case Ok(t):
                    try:
                        return cast(Res[U, E | F], ok(using(t))(E))
                    except catch as f:
                        return cast(Res[U, E | F], err(U)(f))
                case Err(f):
                    return cast(Res[U, E | F], err(U)(f))

        return inner

    return get_catch


def map_err(using: Fn[E, F]):
    """
    Changes the internal `Err` using the function if in an `Err` state. Otherwise it returns
    the `Ok`
    """
    def inner[T](res: Res[T, E]) -> Res[T, F]:

        match res:
            case Ok():
                return cast(Res[T, F], res)
            case Err(e):
                return err(T)(using(e))

    return inner


def and_res[T, U, E](new_res: Res[U, E]) -> Callable[[Res[T, E]], Res[U, E]]:
    """
    Returns the provided result if the old one is `Ok`
    """
    def inner(old_res: Res[T, E]) -> Res[U, E]:

        match old_res:
            case Ok():
                return new_res
            case Err():
                return cast(Res[U, E], old_res)

    return inner


def or_res[T, F](new_res: Res[T, F]) -> Callable[[Res[T, E]], Res[T, F]]:
    """
    Returns the provided result if the current one is an `Err`
    """
    def inner(old_res: Res[T, E]) -> Res[T, F]:

        match old_res:
            case Ok():
                return cast(Res[T, F], old_res)
            case Err():
                return new_res

    return inner


def flatten[T](res: Res[Res[T, E], F]) -> Res[T, E | F]:
    """
    Flattens a `Res` containing a `Res`
    """
    match res:
        case Ok(res):
            return res
        case Err():
            return res


def safe[E](err_type: type[E]):
    """
    Wraps the output `U` of an object or its thrown `Exception` `E` in a
    `Res[U, E]` object. Handles only one `Exception` at a time.
    """

    def inner[U](using: Callable[P, U]) -> Callable[P, Res[U, E]]:

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Res[U, E]:

            try:
                return cast(Res[U, E], ok(using(*args, **kwargs))(err_type))
            except err_type as e:
                return cast(Res[U, E], err(U)(e))

        return wrapper

    return inner


def null_safe[U](using: Callable[P, U | None]):
    """
    Wraps the output of the function in a `Res[T, Nil]` object.
    """

    def inner(*args: P.args, **kwargs: P.kwargs) -> Res[U, Nil]:

        return some(using(*args, **kwargs))

    return inner


def null_and_error_safe(*err_types: type[E]):
    """
    Wraps the output in the `some` function and consumes the error if it is thrown, replacing it with `Nil`
    """

    def inner[T](using: Callable[P, T]):

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Res[T, Nil]:

            try:
                return some(using(*args, **kwargs))
            except err_types as e:
                return map_err(lambda f: Nil(str(f)))(err(T)(e))

        return wrapper

    return inner


q = unwrap