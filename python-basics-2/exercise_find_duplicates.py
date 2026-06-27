# Exercise: Check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# # to store duplicate items
# duplicate = []
# no_duplicate = set(some_list)

# count = 0
# for item_set in no_duplicate:
#     for item_list in some_list:
#         if item_set == item_list:
#             count += 1
#         if count > 1:
#             duplicate.append(item_set)
#             break
#     count = 0
# print(duplicate)

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
