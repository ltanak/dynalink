from dynalink import plugin
print("Step 5: base plugin")

@plugin(name="Base")
class BasePlugin:

    def run(self):
        print("Hello from base plugin")
