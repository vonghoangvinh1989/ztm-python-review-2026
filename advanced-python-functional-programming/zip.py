# zip: combine each item of each list into tuple
my_list = [1, 2, 3]
your_list = [10, 20, 30]
your_list_2 = (10, 20, 30)
their_list = [5, 4, 3]

print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]
print(list(zip(my_list, your_list, their_list)))  # [(1, 10, 5), (2, 20, 4), (3, 30, 3)]
print(list(zip(my_list, your_list_2)))
print(my_list)  # do not modify original data
