print("All numbers between 10 and 20: ")
for y in range(10, 21):
    for x in range(y, -1, -1):
        print(x, end=' ')
    print()

#Even numbers only
print("Even numbers only: ")
for y in range(10, 21, 2):
    for x in range(y, -1, -1):
        print(x, end=' ')
    print()
