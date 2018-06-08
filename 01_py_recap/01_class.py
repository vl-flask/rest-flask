# Objects in Python vs Dictionaries

lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    # We have access to `self` so we can use the data from inside the object.
    # Can use methods
    def total(self):
        return sum(self.numbers)

# A class is essentially a blueprint
# Tells us what data every lottery player has
# and we can personalize it
player1 = LotteryPlayer("Rolf")
player2 = LotteryPlayer("John")
# print(player1==player2)
print(player1.name==player2.name)
# print(player.name)
# print(player.numbers)
# print(player.total())
