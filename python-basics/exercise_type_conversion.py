birth_year = input("what year were you born? ")

from datetime import date

current_year = date.today().year

print(type(birth_year))

age = current_year - int(birth_year)
print(f"Your age is: {age}")
