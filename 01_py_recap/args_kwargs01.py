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
	print("*"*20)
	
# print(what_are_kwargs(12,34, 56))
print(what_are_kwargs(12,34, 56, name="Vassily", city="NYC"))
# print(what_are_kwargs2(12,34, 56, name="Vassily", city="NYC"))
# print(what_are_kwargs3(12,34, 56, name="Vassily", city="NYC"))