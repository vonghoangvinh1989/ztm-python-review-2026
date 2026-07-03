# generators
# range is an example of generators
# range(100)
# list(range(100))


# this will create the whole list in memory and after that it will return
# in ram, will exist this whole list
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(my_list)


print(list(range(1000000)))

# generator work differently, generator using 'yield'
# in ram right now does not have 1 million number, they just have 1 object generator
# ram not store list, just store object generator and generator will yield each item
