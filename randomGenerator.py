import random

for i in range(3):
    # print(random.random())
    print(random.randint(25, 45))


members = ['Mahfuj', 'Rahim', "hello"]
print(random.choice(members))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
