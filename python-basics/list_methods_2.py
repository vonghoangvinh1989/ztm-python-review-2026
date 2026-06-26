basket = ["a", "b", "c", "d", "e", "d"]

# index(value, start, stop) -> find the index of value, can specify where to find at start and stop
print(basket.index("d", 0, 4))

print("d" in basket)
print("x" in basket)
print("i" in "hi my name is Ian")

print(basket.count("d"))
