args = (1, 2, 3)
print(*args)
print(*[1, 2, 3])

data = {"name": "Tom", "age": 20}


def hello(name, age):
    print(name, age)


hello(**data)

# * = open list/tuple into arguments
# ** = open dict into keyword arguments

# print(data)	in cả dict	✅
# print(*data)	unpack keys	✅
# print(**data)	unpack thành keyword args	❌ (với print)
