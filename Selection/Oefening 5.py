number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers will not be tested.")
else:
    test_number = int(input("What final digit do you want to test with"))
    if test_number == (number % 10):
        print(number, "ends with ", test_number)
    else:
        print(number, "does not end with ", test_number)