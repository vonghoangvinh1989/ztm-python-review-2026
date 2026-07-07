# in case we do not specify the mode, it will be reading mode
# with open("test.txt", mode="w") as my_file:
#     text = my_file.write(":)")
#     print(text)

with open("sad.txt", mode="r+") as my_file:
    text = my_file.write(":()")
    print(text)


# note: when we write to the file, the cursor reset
# r+: read + write, overwrite the character that it overlap, cursor set to 0 and overwrite the character
# r+ the file need to be existed first
# a: append
# w: write, overwrite the whole content, can create new file if file does not exist
