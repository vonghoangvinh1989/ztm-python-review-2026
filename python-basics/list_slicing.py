# List slicing
amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]

# list are mutable
amazon_cart[0] = "laptop"
# new_cart = amazon_cart[0:3] # every time we do list slicing, we create a copy of that list
# new_cart = amazon_cart

# if you want to copy a list, not copy the pointer use like this
new_cart = amazon_cart[:]

new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

# note: new_cart = amazon_cart
# copy the reference of amazon_cart to the new_cart (object)
