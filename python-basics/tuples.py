# Tuple (immutable list)
# list but immutable
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[1] = "z"  # it will send error because tuple is immutable

print(my_tuple[1])
print(5 in my_tuple)

# Purpose: if we do not want thing to change, we can use tuple
# for example: store location(lat, long)

# we can use tuple to make the key of dictionary since tuple is immutable
# key of dictionary need to be immutable
user = {(1, 2): [1, 2, 3], "greet": "hello"}
print(user[(1, 2)])
