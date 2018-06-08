# 001 Objects

## Objects vs Dictionaries
Class is like a blueprint. We have access to `self` so we can use the data from inside the object.
```python
lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}
class LotteryPlayer:
    def __init__(self):
        self.name = 'Rolf'
        self.numbers = (5, 9, 12, 3, 1, 21)
    def total(self):
        return sum(self.numbers)
```
An example of method.
```python
player = LotteryPlayer()
print(player.name)
print(player.numbers)
print(player.total())

>>> Rolf
>>> (5, 9, 12, 3, 1, 21)
>>> 51
```
Interesting thing.
```
player1 = LotteryPlayer()
player2 = LotteryPlayer()
print(player1==player2)
print(player1.name==player2.name)
===
Res: False
Res: True
```
Update.
```python
class LotteryPlayer:
    def __init__(self, name):
        self.name = 'Rolf'
        # ...
player1 = LotteryPlayer("Rolf")
player2 = LotteryPlayer("John")
print(player1.name==player2.name)
===
Res: True
```
WHY? - WE PASSED THE `name` PARAMETER, BUT DIDN'T USE IT.  
Let's check it.  
```python
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        # ...
player1 = LotteryPlayer("Rolf")
player2 = LotteryPlayer("John")
print(player1.name==player2.name)
===
RES: False
```

## Student Example
```python
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        c = len(self.marks)
        t = sum(self.marks)
        try:
            return t/c
        except:
            print("An error occured")

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(73)
print(anna.marks)
print(anna.average())
```
