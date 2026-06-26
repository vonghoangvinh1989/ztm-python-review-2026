# Dictionary
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print("basket" in user)  # True
print("size" in user)  # False

# .keys
print("hello" in user.keys())  # False
print("age" in user.keys())  # True

# .values
print("hello" in user.values())  # True

# .items
print(user.items())
print("hello" in user.items())

# .clear, does not return anything
# user.clear()
# print(user)

# .copy
# user2 = user.copy()
# print(user.clear())
# print(user2)

# .pop return the value of what we remove
print(user.pop("age"))
print(user)

# .popItem, remove the last key value pair
print(user.popitem())
print(user)

# update, update the old key or add the new one if it does not exist before
print(user.update({"ages": 55}))
print(user)
