# decorator
def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")

    return wrap_func


@my_decorator
def hello():
    print("hellloooo")


@my_decorator
def bye():
    print("see ya later")


bye()

# under the hood, this is what decorator did, simply wrapping function hello inside and run
# hello2 = my_decorator(hello)
# hello2()
# my_decorator(hello)() # shorter version
