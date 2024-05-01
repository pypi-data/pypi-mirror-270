import inspect
from dataclasses import dataclass
from typing import Callable, Any

def variant(f: Callable[[Any], Any]):
    return f.__annotations__

def alg(f: type):
    for name, value in inspect.getmembers(f):
        if isinstance(value, dict):
            @dataclass
            class Wrapper(f):
                __qualname__ = f.__qualname__ + "." + name
                __annotations__ = value
                pass
            setattr(f, name, Wrapper)
    return f