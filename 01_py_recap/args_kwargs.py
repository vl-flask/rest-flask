# def my_method(arg1, arg2):
    # return arg1 + arg2
	
# print(my_method(5,6))

# # You may want to use more args. In this case, define more args
# def long_method(arg1, arg2, arg3, arg4):
	# pass

# # An option is to use a list
# def my_list_add(list_arg):
	# return sum(list_arg)
	
def add_args(*args):
	sumargs = 0
	for arg in args:
		sumargs += arg
	return sum(args)
	
print(add_args(23, 76, 63, 74,37))

def what_are_kwargs(*args, **kwargs):
	print(args)
	print(kwargs)
	print("*"*20)
def what_are_kwargs2(*args, **kwargs):
	print(f"Args:{args}")
	print(f"Kwargs:{kwargs}")
	print("*"*20)
def what_are_kwargs3(*args, **kwargs):
	print("Args:{}".format(args))
	print("Kwargs:{}".format(kwargs))
	
# print(what_are_kwargs(12,34, 56))
print(what_are_kwargs(12,34, 56, name="Vassily", city="NYC"))
print(what_are_kwargs2(12,34, 56, name="Vassily", city="NYC"))
print(what_are_kwargs3(12,34, 56, name="Vassily", city="NYC"))