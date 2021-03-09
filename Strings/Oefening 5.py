text = input("Enter a text: ")
amount_of_characters = len(text)
triple = 0

for i in range(amount_of_characters - 2):
    if (text[i] == text[i+1]) and (text[i+1] == text[i+2]):
        triple += 1
if triple == 1:
    print("There is one triple in this text.")
elif triple == 0:
    print("There are no triples in this text.")
else:
    print("There are", triple, "triples in this text.")
