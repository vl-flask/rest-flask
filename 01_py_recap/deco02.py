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
print("*"*20)
#

def decorator_w_args(num):
    def my_deco(func):
        @functools.wraps(func)
        def wrapper():
            print("Before the decorated func")
            if num==56:
                print("Not running the func")
            else:
                func()
            print("After the decorated func")
        return wrapper
    return my_deco

@decorator_w_args(56)
def my_function_too():
    print("Hello")
    
my_function_too()
    