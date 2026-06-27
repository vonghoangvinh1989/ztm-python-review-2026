# == check for equality of equality of values
print(True == 1)  # True
print("1" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([1, 2, 3] == [1, 2, 3])  # True

print("--------------------")
# is: check if the location in memory where this value is stored is the same
print(True is 1)  # False
print("1" is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([1, 2, 3] is [1, 2, 3])  # False
print("----------------------")
print(True is True)
print("1" is "1")
print([] is [])  # False, different memory location
print(10 is 10)
print([1, 2, 3] is [1, 2, 3])
