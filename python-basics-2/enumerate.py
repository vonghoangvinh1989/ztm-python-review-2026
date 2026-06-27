# enumerate: use when we need index counter of item we are looping through
for i, char in enumerate("Helllooo"):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate((1, 2, 3)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f"index of 50 is: {i}")
