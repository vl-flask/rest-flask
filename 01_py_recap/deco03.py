import functools
# 
def decorator_w_args(num):
    def my_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Before the decorated func")
            if num==56:
                print("Not running the func")
            else:
                func(*args, **kwargs)
            print("After the decorated func")
        return wrapper
    return my_deco

@decorator_w_args(32)
def my_function_too(x, y):
    print(x+y)
    
my_function_too(57, 67)