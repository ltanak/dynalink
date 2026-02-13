from dynalink import plugin
print("Step 7: function pluging")

@plugin(name="Function", kind="callable")
def function_plugin():
    print("We're testing the assumptions of the plugin registry!")
