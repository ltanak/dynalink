# import inspect

# class RunnablePluginMeta(type):

#     def __new__(mcls, clsname, bases, clsdict):

#         if not inspect.isclass(mcls):
#             raise TypeError(f"Object with name '{clsname}' is not a class")
#         if not (callable(clsdict["run"]) and )



#         cls = super().__new__(mcls, clsname, bases, clsdict)
#         return cls
