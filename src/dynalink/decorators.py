from typing import Callable, TypeVar
from dynalink.core import registry
print("Step 2: get decorator")

T = TypeVar("T") # generics in python

def plugin(name: str, kind: str) -> Callable[[T], T]:
    """
    Registers a plugin with the given name
    :param name: Description
    :type name: str
    :return: Description
    :rtype: Callable[[T], T]
    """
    def decorator(object: T) -> T:
        registry.register(name, kind, object)
        return object
    
    return decorator

print("Step 3: end decorator")