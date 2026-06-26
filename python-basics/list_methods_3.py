basket = ["a", "x", "b", "c", "d", "e", "d"]

# sort work in place, return None
# basket.sort()

# sorted() does not wort the basket in place, it create a copy of basket and sort it
# sorted will return a new array
print(sorted(basket))
print(basket)

# sorted is the same at using the below three lines
# new_basket = basket[:]
new_basket = basket.copy()  # instead of using basket[:], we can use copy()
new_basket.sort()
print(new_basket)

# reverse will reverse the item in basket, work in place, we can sort first and reverse
basket.sort()
basket.reverse()
print(basket)
