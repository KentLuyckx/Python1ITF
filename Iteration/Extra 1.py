end_number = int(input("Up to which limit would you like to print the sequence of Fibonacci? "))
first_number = 0
second_number = 1
third_number = 1

print(first_number, end=" ")
print(second_number, end=" ")
while end_number >= third_number:
    print(third_number, end=" ")
    first_number = second_number
    second_number = third_number
    third_number = first_number + second_number
