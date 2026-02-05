from dynalink.core import registry

print("Base plugin ran!")

class BasePlugin:
    name = "Base Plugin"

    def run(self):
        print("Hello from base plugin")


registry.register("base", BasePlugin())
