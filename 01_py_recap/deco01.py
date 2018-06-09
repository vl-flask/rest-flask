# Decorators

## Just a function 
## First import it

import functools

def my_decorator(func):
    @functools.wraps(func)
    def func_that_runs_func():
        print("From the decorator")
        # Make sure you always call the func from the decorator
        func()
        print("After the decorator")
    return func_that_runs_func

@my_decorator
def my_func():
    print("I'm a function")
    
my_func()

