# OOP
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    # we can use without instantiate it
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    # we can use when we do not care about the class state
    @staticmethod
    def adding_things_2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Tom", 10)
print(player1.adding_things(2, 3))

# player3 = PlayerCharacter.adding_things_2(2, 3)
# print(player3)
