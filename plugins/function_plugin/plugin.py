from dynalink.core import registry

print("Function plugin ran!")

def function_plugin():
    print("We're testing the assumptions of the plugin registry!")



registry.register("function", function_plugin)
