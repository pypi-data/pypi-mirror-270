"""
Module for handling tuples without risk of panics
"""
from typing import Tuple
from pythonix.op import item
from pythonix.res import safe, null_and_error_safe
from enum import Enum


class Side(Enum):
    LEFT: str = "LEFT"
    RIGHT: str = "RIGHT"


def new[T](*elements: T) -> Tuple[T, ...]:
    """
    Convenience function to create a new series of data of a given type
    """
    return elements


def push(side: Side = Side.RIGHT):
    """
    Push an element to either side of a `Tuple`
    """
    def get_element[U](element: U):
        
        def inner[T](tuples: Tuple[T, ...]) -> Tuple[T | U, ...]:

            match side:
                case Side.LEFT:
                    return (element,) + tuples
                case Side.RIGHT:
                    return tuples + (element,)

        return inner

    return get_element


def get(index: int):
    """
    Retrieve an element from a `Tuple` at the provided index
    """
    def inner[T](tuples: Tuple[T, ...]):

        return item(index)(tuples)

    return inner


def extend(side: Side = Side.RIGHT):
    """
    Combine two tuple series together
    """
    def get_left[T](new: Tuple[T, ...]):

        def get_right[U](old: Tuple[U, ...]) -> Tuple[T | U, ...]:

            match side:
                case Side.LEFT:
                    return new + old
                case Side.RIGHT:
                    return old + new

        return get_right

    return get_left


def index[T](element: T):
    """
    Find the index of an element in `Tuple` if it exists
    """
    @null_and_error_safe(ValueError)
    def inner(tuples: Tuple[T, ...]) -> int:

        return tuples.index(element)

    return inner


def count_occurrences[T](value: T):
    """
    Count the occurrences of the provided value in a `Tuple`
    """
    def inner(tuples: Tuple[T, ...]) -> int:

        return tuples.count(value)

    return inner


def insert(index: int):
    """
    Recreate the `Tuple` with the provided element at the index
    """
    def new_item[U](insert: U):

        def inner[T](tuples: Tuple[T, ...]) -> Tuple[T | U, ...]:
            return tuples[:index] + (insert,) + tuples[index:]
        
        return inner
    
    return new_item


def remove(index: int):
    """
    Recreate the `Tuple` without the element at the provided index
    """
    @safe(IndexError)
    def inner[T](tuples: Tuple[T, ...]) -> Tuple[T, ...]:
        if index > (length := len(tuples)):
            raise IndexError(f'Incompatible index {index} is greater than length {length}')
        return tuples[:index] + tuples[index+1:] 
    return inner


push_left = push(Side.LEFT)
push_right = push(Side.RIGHT)
last = get(-1)
first = get(0)
extend_left = extend(Side.LEFT)
extend_right = extend(Side.RIGHT)
