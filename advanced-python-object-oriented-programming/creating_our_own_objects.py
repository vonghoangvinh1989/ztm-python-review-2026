# OOP
# self: refer is whatever to the left of the 'dot' or .
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print("run")
        return "done"


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)

print(player1.name)
print(player1.age)
print(player1.run())

print(player2.name)
print(player2.age)
player2.attack = 50

print(player2.attack)
print(player1.attack)
