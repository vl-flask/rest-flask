def methodception(func):
    return func()

def add_two_numbers():
    return 35 + 77

#print(methodception(add_two_numbers))

#print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 484]

# Remove all even elements
# Now let's 'filter' it.
print(list(filter(lambda x: x%2==0, my_list)))
# Same as
def not_13(x):
    return x != 13
print(list(filter(not_13, my_list)))
# Very similar to list comprehensions
compr = [x for x in my_list if x!=13]
print(compr)

(lambda x: x*3)(5)

def f(x):
    return x*3
f(5)