basket = [1, 2, 3, 4, 5]

# adding
# append change the list in place - it does not produce a value
# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

# insert modify list in place - it does not produce a value
# basket.insert(5, 100)
# print(basket)

# extend
new_list = basket.extend([100])
# print(basket)
# print(new_list)

# removing
# pop() will pop the last index, pop(index) pop the exact indext
# and pop() return whatever value they pop out
# basket.pop()
new_list = basket.pop(0)
# print(basket)
print(new_list)

# remove(value) will remove the value put in, working in place
new_list = basket.remove(4)
print(basket)
print(new_list)

# clear remove whatever in the list
basket.clear()
print(basket)
