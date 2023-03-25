import requests

def first_function():
    pass

class Human:
    pass

rq = requests
first_f = first_function
nick = Human

print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)

class First_class:
    pass

class Second_class(First_class):
    pass

print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))

import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
