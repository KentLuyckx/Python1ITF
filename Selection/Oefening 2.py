birth_year = int(input("Enter your year of birth"))
current_year = int(2020)

if current_year - birth_year >= 18:
    print("Your age is =", current_year - birth_year)
    print("So, you're an adult")
else:
    print("Your age is=", current_year - birth_year)
    print("You're not an adult yet")