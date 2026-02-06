import plugins.base_plugin.plugin
print("Step 6: back to main")
import plugins.function_plugin.plugin
print("Step 8: back to main")

#below was already ran, so not ran again
from dynalink.core import registry

def main():
    print("MAIN file!")
    plugin_cls = registry.get("Base")

    plugin = plugin_cls()
    print(type(plugin_cls))
    print(type(plugin))
    plugin.run()

    function = registry.get("Function")
    print(type(function))
    function()


if __name__ == "__main__":
    main()
