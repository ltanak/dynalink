import plugins.base_plugin.plugin
import plugins.function_plugin.plugin

from dynalink.core import registry

def main():
    print("main file!")
    plugin = registry.get("base")
    plugin.run()

if __name__ == "__main__":
    main()
