weight = int(input("Your weight in kilograms: "))
length = int(input("Your length in centimeters: "))
bmi = (weight / (length ** 2)) * 10000

print("A person of", weight, "kg with a length of", length, "cm has a bmi of", bmi)
if bmi < 18:
    print("You are underweight.")
elif 18 <= bmi <= 25:
    print("You have a normal weight.")
elif 25 <= bmi <= 27:
    print("You are slightly overweight.")
elif 27 <= bmi <= 30:
    print("You are moderately overweight.")
elif 30 <= bmi <= 40:
    print("You are obese.")
else:
    print("You are sickly obese.")
