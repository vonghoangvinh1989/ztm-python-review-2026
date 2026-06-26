my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# # difference
# print(my_set.difference(your_set))

# # discard
# print(my_set.discard(5))
# print(my_set)

# difference_update, modify my_set
# print(my_set.difference_update(your_set))
# print(my_set)

# print(my_set.intersection(your_set))
# print(my_set & your_set)

# two sets have no elmenents in common
# True -> no overlap (completely different)
# # False -> at least oone comment element
# print(my_set.isdisjoint(your_set))  # False

# # union, unite two sets
# print(my_set.union(your_set))
# print(my_set | your_set)  # shorthand

my_set2 = {4, 5}
your_set2 = {4, 5, 6, 7, 8, 9, 10}
print(my_set2.issubset(your_set2))  # True
print(my_set2.issuperset(your_set2))  # False
print(your_set2.issuperset(my_set2))  # True
