number = int(input("Enter a positive number: "))

print(number, end=' ')
while number != 0:
    number = number - 1
    print('..', number, end=' ')
