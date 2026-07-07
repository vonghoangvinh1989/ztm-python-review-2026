# file reading has the idea called cursor to read the content of the file
# my_file = open("test.txt")
# print(my_file.read())  # at this point the cursor at the end of file

# my_file.seek(0)  # move the cursor back to the beginning
# print(my_file.read())

# my_file.seek(0)
# print(my_file.read())

my_file = open("test.txt")
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# readlines give the list of content of each lines
print(my_file.readlines())

my_file.close()


# note
# .read() -> read whole file
# .readline() -> read one line, process each line
# .readlines() -> read all lines, make into a list
