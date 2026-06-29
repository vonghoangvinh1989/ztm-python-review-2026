# OOP
# self: refer is whatever to the left of the 'dot' or .
class PlayerCharacter:
    # Class Object Attribute
    membership = True  # use when no change

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attributes
            self.age = age

    def run(self):
        print("run")
        return "done"

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50

# help function show blueprint of class
# help(player1)

print(player1.shout())
print(player2.shout())
# print(player2.membership)
# print(player1.name)
