class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)

        # we can use super overhere has the same action as User.__init__() but we do not
        # need to pass the 'self' inside
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")


# instrospection: determine the type of object in run time
wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
print(dir(wizard1))
