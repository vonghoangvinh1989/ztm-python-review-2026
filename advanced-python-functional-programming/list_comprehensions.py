# list comprehensions
# my_list = []
# for char in "hello":
#     my_list.append(char)
# print(my_list)

# syntax: [param for param in iterable]
my_list = [char for char in "hello"]
my_list_2 = [num for num in range(0, 100)]
my_list_3 = [num**2 for num in range(0, 100)]

# syntax: [param for param in iterable if condition ]
my_list_4 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list)
# print(my_list_2)
# print(my_list_3)
print(my_list_4)
