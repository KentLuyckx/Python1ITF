string = input("Enter a string: ")
position_star = string.find("*")

while position_star != -1:
    string = string[0:position_star-1] + string[position_star+2:]
    position_star = string.find("*")
print(string)
