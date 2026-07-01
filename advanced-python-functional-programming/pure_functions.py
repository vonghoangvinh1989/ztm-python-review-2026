# pure function: same input, always return same output
# function should not produce any side effect (affect outside world)
wizard = {"name": "Merlin", "power": 50}


def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by_2([1, 2, 3]))
