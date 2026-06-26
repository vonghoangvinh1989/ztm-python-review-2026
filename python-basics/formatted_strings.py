# formatted strings

name = "Johnny"
age = 55
# print("hi " + name + ". You are " + str(age) + " years old")
print(f"hi {name}. You are {age} years old")

# python 2 way
print("hi {new_name}. You are {age} years old".format(new_name="sally", age=100))
