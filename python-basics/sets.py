# set: unordered collections of unique objects
my_set = {1, 2, 3, 4, 5}  # no duplicate
my_set.add(100)
my_set.add(2)
print(my_set)

# print(my_set[0])  # show error

print(1 in my_set)
print(len(my_set))

# convert list into set (to remove duplicate)
# my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))

# convert set to list
print(list(my_set))

# copy
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)
