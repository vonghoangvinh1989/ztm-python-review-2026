# from utility import multiply, divide
# from shopping.more_shopping import shopping_cart

# # note: import need to be clear, not good to import something as * (from utility import *)

# if __name__ == "__main__":
#     print(shopping_cart.buy("apple"))
#     print(divide(5, 2))
#     print(multiply(5, 2))
#     print(max([1, 2, 3]))

#     print("please run this")

# import random

# # give a random number between 0 - 1
# print(random.random())

# # give a random number between 1 - 10
# print(random.randint(1, 10))

# # pick one from the list
# print(random.choice([1, 2, 3, 4, 5]))


# from random import shuffle

# my_list = [1, 2, 3, 4, 5]
# print(shuffle(my_list))
# print(my_list)

import sys

# actually the file name
print(sys.argv[0])

first = sys.argv[1]
last = sys.argv[2]
print(f"hiiiii! {first} {last}")
