from dynalink.decorators import plugin
print("Step 4: global plugin")
__all__ = ["plugin"]

# makes it so that all plugin authors write from dynalink import plugin
# instead of from dynalink.decorators import plugin