from typing import Callable

type Fn[T, U] = Callable[[T], U]
type FnOnce[U] = Callable[[], U]
