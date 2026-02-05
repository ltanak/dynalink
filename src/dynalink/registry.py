from typing import Dict, Any

class PluginRegistry:
    """
    storage for all registered plugins

    plugins optinto the registry
    """

    def __init__(self):
        self._plugins: Dict[str, Any] = {}

    def register(self, name: str, plugin: Any) -> None:
        if name in self._plugins:
            raise ValueError(f"Plugin '{name}' already registered")

        self._plugins[name] = plugin

    def get(self, name: str) -> Any:
        return self._plugins[name]

    def all(self) -> Dict[str, Any]:
        return dict(self._plugins)
