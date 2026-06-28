def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
