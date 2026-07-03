# iterable: object in python able to loop through __iter__
# iterate: act taking item from iterable
# generators is iterable but not everything iterable is generators, for example
# range: generator -> iterable, but list is not
def generator_function(num):
    for i in range(num):
        yield i * 2  # stop the function, and come back when we do something, call next()


g = generator_function(100)
# g = generator_function(1)
next(g)
next(g)
print(next(g))
print(next(g))


# going one by one, just held one item in it, and for will call next behind the scene
# for item in generator_function(1000):
#     print(item)
