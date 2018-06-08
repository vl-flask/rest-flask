# Static and Class Methods

## Problem
We have our student class. Let's add something like the `go_to_school()` method.
```python
class Student:
    # [...]
    def go_to_school(self):
        print(f"I'm going to school")

anna = Student("Anna", "MIT")
anna.go_to_school()
===
RES: I'm going to school
```
Okay, let's remove it
```python
class Student:
    # [...]
    def go_to_school(self):
        print(f"I'm going to school")

anna = Student("Anna", "MIT")
anna.go_to_school()
===RES:
TypeError: go_to_school() takes 0 positional arguments but 1 was given
```

## Class Methods
Solution 1: Use class methods, and `cls` instead of `self` as the argument.
```python
class Student:
    # [...]
    @classmethod
    def go_to_school(cls):
        print(f"I'm going to school")
        print(f"I'm a {cls}")

anna = Student("Anna", "MIT")
anna.go_to_school()
===RES:
(rest) $ python 01*/02*
I'm going to school
I'm a <class '__main__.Student'>
```

## Static Methods
That's option 2.
```python
class Student:
    # [...]
    @staticmethod
    def go_to_school():
        print(f"I'm going to school")

anna = Student("Anna", "MIT")
anna.go_to_school()
===RES:
(rest) $ python 01*/02*
I'm going to school
```
## Call as a Class
With both static and class methods, you can simply do like that:
```python
Student.go_to_school()
===RES:
I'm going to school
```
