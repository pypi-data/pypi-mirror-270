"""
Module for handling key value pairs.
"""

from typing import NamedTuple, Tuple, TypeVar
from pythonix.internals.types import Fn

type Pairs[V] = Tuple[Pair[V], ...]

T = TypeVar("T")

class Pair[V](NamedTuple):
    """
    A typed key value pair whose key is a `str`
    """
    key: str
    value: V


def new[V](key: str) -> Fn[V, Pair[V]]:
    """
    Create a new `Pair` safely 
    """
    def get_value(value: V):

        return Pair(key, value)

    return get_value


def set_key(key: str):
    """
    Creates a new `Pair` from a provided one with the provided key.
    """
    def get_pair[V](pair: Pair[V]) -> Pair[V]:

        return new(key)(pair.value)

    return get_pair


def set_value[W](value: W):
    """
    Creates a new `Pair` with a new value, preserving its key.
    """
    def get_pair[V](pair: Pair[V]) -> Pair[W]:

        return new(pair.key)(value)

    return get_pair

def get_value[V](pair: Pair[V]) -> V:
    """
    Retrieves the `value` of a provided `Pair`
    """
    return pair.value

def get_key[V](pair: Pair[V]) -> str:
    """
    Retrieves the `key` of a provided `Pair`
    """
    return pair.key


def map[V, W](using: Fn[V, W]):
    """
    Change the inner value of a `Pair` with a function
    """
    def inner(pair: Pair[V]) -> Pair[W]:
        return set_value(using(pair.value))(pair)
    
    return inner