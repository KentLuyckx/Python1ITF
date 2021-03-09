string = input("Enter a text: ")
search = "in"

if string.startswith(search) or string.startswith(search, 1):
    print("'in' appears in the first or second place")
elif search in string:
    print("'in' appears in the word, but not in front")
else:
    print("This word does not contain 'in'")
