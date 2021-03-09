age_son = int(input("How old are you? "))
age_father = int(input("How old is your dad? "))
amount_of_years = 0

while age_father != (age_son * 2) and age_father <= 120:
    age_father = age_father + 1
    age_son = age_son + 1
    amount_of_years = amount_of_years + 1
if age_father == (age_son * 2):
    print("Within", amount_of_years, "years, your father will be twice your age.")
    print("Your father will be", age_father, "and you will be", age_son,".")
else:
    print("This situation is no longer possible for your ages.")
