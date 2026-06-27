# iterable: objects/collections (list, dictionary, tuple, set, string) they can be iterated -> one by one check
# each item in the collection
user = {"name": "Golem", "age": 5006, "can_swim": False}

# common pattern for using items()
for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# int object can not be iterable
for item in 50:
    print(item)
