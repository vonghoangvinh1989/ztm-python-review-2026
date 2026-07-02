def hello(func):
    func()


def greet():
    print("still here!")


a = hello(greet)

print(a)


# decorator happens because function can pass like a variable
# @decorator
# def hello():
#     pass
