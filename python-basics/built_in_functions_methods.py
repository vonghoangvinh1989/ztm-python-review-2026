greet = "hellloooo"
print(greet[0 : len(greet)])

# methods: owned by something
# for example: string methods

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))

# string immutable, so above methods create new strings
print(quote)
