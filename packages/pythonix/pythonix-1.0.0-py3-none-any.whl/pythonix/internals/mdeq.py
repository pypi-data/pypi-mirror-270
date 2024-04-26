"""
### MDeq

Functions used to create and perform operations safely on a singly typed mutable linked list.

"""
from collections import deque
from __future__ import annotations
from typing import Callable, Iterable
from pythonix.res import null_and_error_safe, safe, Ok

class MDeq[T](object):
    """
    `MDeq` is a singly-typed mutable linked list. `push` and `pop` operations are thread safe and run in
    `O(1)` time. Insert and get operations run in `O(n)` time. As a mutable data structure there are some
    rules to keep in mind.

    #### Rules
    - Only share one reference to a `MDeq` at a time
    - Use the `copy` function to share copies of it if necessary
    - Use the `pipes.Do` class to perform consecutive functions on it

    #### Example
    ```python
    data = mdeq.new(int)(1, 2, 3, 4, 5, 6)
    (
        pipes.Do(data)
        (md.push(7))
        (md.push(8))
        (md.push(9))
    )
    ```
    """

    inner: deque[T] = deque()

    def __init__(self, *args: T):
        self.inner = deque(args)


def new[T](*vals: T) -> MDeq[T]:
    """
    Creates a new instance of `MDeq` with the `vals` passed in.
    Make sure all the types are the same or you'll have weird type hints.
    """
    return MDeq(*vals)


def push[T](element: T) -> Callable[[MDeq[T]], Ok[None]]:
    """
    Pushes a new element `T` to the end of an `MDeq`.
    """

    def inner(deq: MDeq[T]) -> Ok[None]:
        """
        Specify the `MDeq` that will receive the new element.
        """
        deq.inner.append(element)
        return Ok(None)

    return inner


def pushleft[T](element: T) -> Callable[[MDeq[T]], Ok[None]]:
    """
    Pushes a new element `T` to be the new first element in an `MDeq`
    """

    def inner(deq: MDeq[T]) -> Ok[None]:
        deq.inner.appendleft(element)
        return Ok(None)

    return inner


def insert[T](element: T):
    """
    Inserts a new element at the provided index. Runs on `O(n)` time.

    Provide the new element `T`
    """

    def get_at(index: int):
        """
        Now provide the index.
        """

        def inner(deq: MDeq[T]) -> Ok[None]:
            """
            Now provide the `MDeq`
            """
            deq.inner.insert(index, element)
            return Ok(None)

        return inner

    return get_at


def copy[T](deq: MDeq[T]) -> MDeq[T]:
    """
    Returns a shallow copy of the `MDeq` as a new object.
    """
    return new(*deq.inner.copy())


@null_and_error_safe(IndexError)
def pop[T](deq: MDeq[T]) -> T:
    """
    Removes and returns the last element in an `MDeq` if it exists.
    """
    return deq.inner.pop()


@null_and_error_safe(IndexError)
def popleft[T](deq: MDeq[T]) -> T:
    """
    Removes and returns the first element in an `MDeq` if it exists.
    """
    return deq.inner.popleft()


@null_and_error_safe(IndexError)
def first[T](deq: MDeq[T]) -> T:
    """
    Returns the first element in an `MDeq` if it exists.
    """
    return deq.inner[0]


@null_and_error_safe(IndexError)
def last[T](deq: MDeq[T]) -> T:
    """
    Returns the last element in an `MDeq` if it exists.
    """
    return deq.inner[-1]


def at(index: int):
    """
    Returns the element at the provided index in an `MDeq` if it exists.
    """

    @null_and_error_safe(IndexError)
    def inner[T](deq: MDeq[T]) -> T:

        return deq.inner[index]

    return inner


def remove(index: int):
    """
    Removes the element from the `MDeq` if it exists at the given index.
    """

    @safe(IndexError)
    def inner[T](deq: MDeq[T]) -> None:

        del deq.inner[index]

    return inner


def extend[T](src: Iterable[T]):
    """
    Combines an iterable with a provided `MDeq` with all new elements being appended.
    """

    def inner(tgt: MDeq[T]) -> Ok[None]:

        tgt.inner.extend(src)
        return Ok(None)

    return inner


def extendleft[T](src: Iterable[T]):
    """
    Combines an iterable with a provided `MDeq` with all new elements going first.
    """

    def inner(tgt: MDeq[T]) -> Ok[None]:

        tgt.inner.extendleft(src)
        return Ok(None)

    return inner


def index[T](find: T, start: int = 1):
    """
    Retrieves the index of the provide dvalue, if it exists.
    """

    @null_and_error_safe(ValueError)
    def inner(deq: MDeq[T]) -> int:

        return deq.inner.index(find, start)

    return inner
