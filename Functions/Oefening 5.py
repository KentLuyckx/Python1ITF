def count(string):
    result = [0, 0]
    for letter in string:
        if letter.isupper():
            result[0] += 1
        elif letter.islower():
            result[1] += 1
    return result

# Basis Oefening:
# text = input("Your string: ")
# result = count(text)

# print("Capitals = {}".format(result[0]))
# print("Lower case letters = {}".format(result[1]))


# Uitbreiding:
password = input("Set your password (at least 2 uppercase and 3 lowercase letters): ")
result = count(password)

while (result[0] < 2) or (result[1] < 3):
    password = input("Set your password (at least 2 uppercase and 3 lowercase letters): ")
    result = count(password)
print("Your password has been set to {}".format(password))