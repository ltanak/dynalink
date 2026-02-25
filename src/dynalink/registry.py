from typing import Dict, Any
from collections import defaultdict
import inspect

from .contracts import RunnablePlugin
print("Step 0: import the PluginRegistry class")

class PluginRegistry:
    """
    storage for all registered plugins
    plugins optinto the registry
    """

    def __init__(self):
        self._plugins: Dict[tuple[str, str], Any] = {}
        self._names: Dict[str, list[str, str]] = defaultdict(list) # in case there are multiple names, lists out all the names and their kinds
        self._kinds: Dict[str, list[str, str]] = defaultdict(list) # in case for multiple kinds, lists out all their names

    def register(self, name: str, kind: str, plugin: Any) -> None:
        if (name, kind) in self._plugins:
            raise ValueError(f"Plugin '{name}' with kind '{kind}' already registered")
        
        self._validate_kind(name, kind, plugin)

        key = (name, kind)
        self._plugins[key] = plugin
        self._names[name].append(key)
        self._kinds[kind].append(key)

    def _validate_kind(self, name: str, kind: str, obj: Any):
        if kind == "callable":
            if not (callable(obj) and not inspect.isclass(obj)):
                raise TypeError(f"Input kind was {kind}, object '{name}' was not a callable.")
        # all class validation handled via metaclass
        if kind == "runnable":
            if not inspect.isclass(obj) or not issubclass(obj, RunnablePlugin):
                raise TypeError("Class does not inherit from the RunnablePlugin class")

    def get(self, name: str, kind: str) -> Any:
        return self._plugins[(name, kind)]
    
    def get_all_kinds(self, kind: str):
        return self._kinds[kind]
    
    def get_all_names(self, name: str):
        return self._names[name]

    def all(self) -> Dict[(str, str), Any]:
        return dict(self._plugins)
