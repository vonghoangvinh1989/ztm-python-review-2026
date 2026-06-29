# Exercise Cats Everywhere
# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat("Lily", 5)
cat2 = Cat("Tom", 25)
cat3 = Cat("Meow", 30)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# Solution with lambda
def oldest_cat2(cats):
    return max(cats, key=lambda cat: cat.age)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
oldest = oldest_cat(cat1.age, cat2.age, cat3.age)
print(f"The oldes cat is {oldest} years old.")

found_oldest_cat = oldest_cat2([cat1, cat2, cat3])
print(f"The oldes cat is {found_oldest_cat.age} years old.")
