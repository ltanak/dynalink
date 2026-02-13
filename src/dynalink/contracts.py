import inspect

class RunnablePluginMeta(type):

    def __new__(mcls, clsname, bases, clsdict):
        # clsdict / namespace only contains attributes defined in this classbody
        if not inspect.isclass(mcls):
            raise TypeError(f"Object with name '{clsname}' is not a class")
        if "run" not in clsdict:
            raise TypeError(f"Object with name '{clsname}' must define 'run(...)")
        if not (callable(clsdict["run"])): # IMPORTANT: ADD CHECK TO MAKE SURE THAT THE RUN METHOD IS FROM THE CURRENT CLASS AND IS NOT AN INHERITED ATTRIBUTES
            raise TypeError(f"Object with name '{clsname}' does not have a 'run(...)' method")
        
        cls = super().__new__(mcls, clsname, bases, clsdict)
        return cls

class RunnablePlugin(metaclass=RunnablePluginMeta):
    
    def run(self):
        pass