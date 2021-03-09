color = input("What is your favorite color? ")
length = len(color)
x = 0
y = 0

print(color[:3:2])
print("This color contains", length, "letters")
print('')
while x < len(color):
    print(color[x], "=", ord(color[x]))
    x += 1
print('')
for y in range(len(color)):
    if y % 2 == 0:
        print("#", color[y], "#")
    else:
        print("**", color[y], "**")
