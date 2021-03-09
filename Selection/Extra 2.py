name = input("Enter your name: ")
first_digits = int(input("Enter the first 9 digits of your national number: "))
last_digits = int(input("Enter the last 2 digits of your national number: "))

control_number = (first_digits % 97)
control = 97 - control_number
if last_digits != control:
    print("Hello", name, "the national number you entered is not correct. ")
else:
    year = first_digits // 10000000
    month = (first_digits % 10000000)//100000
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    else:
        month = "December"
day = (first_digits // 1000) % 100
gender = (first_digits // 1) % 1000
if gender % 2 == 0:
    gender = "female."
else:
    gender = "male."
if last_digits == control:
    print("Hello", name, "your gender is", gender)
    print("You were born on", day, month,  year)
