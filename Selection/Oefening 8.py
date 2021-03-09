number_of_pizzas = int(input("How many pizzas are there: "))
number_of_wine = int(input("How many bottles of wine are there: "))

if number_of_pizzas < 5 or number_of_wine < 5:
    print("This is just a stupid party.")
else:
    if number_of_pizzas >= (number_of_wine * 2) or number_of_wine >= (number_of_pizzas * 2):
        print("This is a fantastic party.")
    else:
        print("This is a good party.")

