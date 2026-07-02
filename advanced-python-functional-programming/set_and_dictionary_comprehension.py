# set comprehension
my_set = {char for char in "hello"}
my_set_2 = {num for num in range(0, 100)}
my_set_3 = {num**2 for num in range(0, 100) if num % 2 == 0}
print(my_set)
print(my_set_2)
print(my_set_3)

# dictionary comprehension
simple_dict = {"a": 1, "b": 2}
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict_2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)
print(my_dict_2)
