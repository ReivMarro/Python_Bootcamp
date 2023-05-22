fav_books = ["Mistborn", "Wheel of Time", "LotR"] 
# This could be a set and could be casted, using fav_books = set(fav_books)
# This could be a tuple and could be casted, using fav_books = tuple(fav_books)

for book in fav_books:
    print(book)   # This is the basic way
# This means: for item in my iterable
#  you can do something with set item

# Fancier way to do this:
for book in fav_books:
    print(f"{book} is one of my favourite books")

# This can be mixed with a conditional operator too. For example:
for books in fav_books:
    if books == "LotR":
        book = input("Which book from the trilogy would you like? ")
        print(f"You ordered {book} from LotR")


# We could also make a subscriptable string out of this
title = "Mistborn"
for letter in title:
    print(letter)

# We could also loop through dictionaries
person = {
    "name": "JMR",
    "instagram": "@MRJ",
    "twitter": "JRM"
}
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")
