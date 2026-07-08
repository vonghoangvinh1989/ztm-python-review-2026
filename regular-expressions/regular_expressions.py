import re

pattern = re.compile("search this inside of this text please")
string = "search this inside of this text please! Vinh Vong"

# match object when using regular expression
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

# print(a.span())  # return a tuple showing the index of found (17, 21)
# print(a.start())  # when the text found start
# print(a.end())  # when the text found end
# print(a.group())
print(b)

# return object only full match, the search string and compile is exactly the same
# print(c)

# print(d)
