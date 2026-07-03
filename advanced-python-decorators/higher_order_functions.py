# higher order function HOC
# function accepts a function as a parameter
def greet(func):
    func()


# function return another function
def greet2():
    def func():
        return 5

    return func


# note: map, filter, reduce also are higher order functions
