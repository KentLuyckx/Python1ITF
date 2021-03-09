def calculate_discount(membership_fee):
    return membership_fee * 0.9


for i in range(4):
    print("Information for member", i+1)
    name = input("Name: ")
    age = int(input("Age: "))
    amount_of_years = int(input("Member for how many years: "))
    membership_fee = 0
    if age < 12:
        membership_fee = 20
    elif 12 <= age <= 18:
        membership_fee = 50
    else:
        membership_fee = 95
    if amount_of_years >= 5:
        membership_fee = calculate_discount(membership_fee)
    print("Member fee for", name, "=", membership_fee)

