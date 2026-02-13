from dynalink.decorators import plugin
from dynalink.contracts import RunnablePlugin
print("Step 4: global plugin")
__all__ = ["plugin", "RunnablePlugin"]

# makes it so that all plugin authors write from dynalink import plugin
# instead of from dynalink.decorators import plugin