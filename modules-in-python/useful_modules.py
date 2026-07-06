from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 4, 5, 6, 7, 7]
# sentence = "blah blah blah thinking about python"

# # create a dictionary to count each item appears how many time in list
# print(Counter(li))
# print(Counter(sentence))

# dictionary = defaultdict(lambda: "does not exist", {"a": 1, "b": 2})
# print(dictionary["a"])
# print(dictionary["b"])
# print(dictionary["c"])
# print(dictionary)

d = OrderedDict()
d["a"] = 1
d["b"] = 2

d2 = OrderedDict()
d["a"] = 2
d["b"] = 1

print(d2 == d)

d3 = {"c": 100}
d["a"] = 1
d["b"] = 2

d4 = {"c": 100}
d["a"] = 2
d["b"] = 1

print(d3 == d4)
