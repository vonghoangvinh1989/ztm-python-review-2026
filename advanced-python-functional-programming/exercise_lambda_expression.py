my_list = [5, 4, 3]

# square
new_list = list(map(lambda item: item**2, my_list))
print(new_list)

# list sorting based on the second item of tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)
