my_tuple = (1, 2, 3, 4, 5, 5)
new_tuple = my_tuple[1:4]
print(new_tuple)

# assign tuple
x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

# count
print(my_tuple.count(5))

# index
print(my_tuple.index(5))

# len
print(len(my_tuple))
