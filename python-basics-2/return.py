def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)
    return 5  # never run
    print("hello")  # never run


# should do one thing really well
# should return something
# print(sum(10, sum(10, 5)))

total = sum(10, 20)
print(total)
