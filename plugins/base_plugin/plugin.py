from dynalink import plugin, RunnablePlugin
print("Step 5: base plugin")

@plugin(name="Base", kind="runnable")
class BasePlugin(RunnablePlugin):

    def run(self):
        print("Hello from base plugin")

    