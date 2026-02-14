from typing import Callable, TypeVar, Any
from dynalink.core import registry
import inspect

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
        if kind == "callable":
            _validate_callable(name, object)
        registry.register(name, kind, object)
        return object
    
    return decorator

def _validate_callable(name: str, obj: Any):
    if not callable(obj):
        raise TypeError(f"Object '{name}' is not of type callable, when it is expected to be a callable.")
    
    signature = inspect.signature(obj)
    params = signature.parameters
    return_type = signature.return_annotation


print("Step 3: end decorator")