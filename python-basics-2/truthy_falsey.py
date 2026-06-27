is_old = bool("hello")
is_licenced = bool(5)

password = "123"
username = "johnny"

# print(bool(""))
# print(bool(0))
# print(bool(None))

# Falsy: 0, "", None, {}, [], ...

if password and username:
    print("you are old enough to drive, and you have a license!")
else:
    print("you are not of age!")
    print("okoko")
