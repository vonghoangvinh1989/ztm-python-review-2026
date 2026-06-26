# Dictionary
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

# instead of user["age"], we can use method .get("age") to avoid generate error if age does
# not exist --> return None, we can set the default value with get also
print(user.get("age", "55"))

# another way to create dictionary
user2 = dict(name="JohnJohn")
print(user2)
