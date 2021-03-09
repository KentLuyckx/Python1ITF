string = input("Enter a text: ")

if string.rfind("x") < string.rfind("y"):
    print("In this text every x is followed by a y")
else:
    print("In this text not every x is followed by a y")
