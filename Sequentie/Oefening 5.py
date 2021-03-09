exchange_rate = float(input("Enter the current exhange dollar rate (€ -> $): "))
euro_amount = float(input("Enter your amount of Euros: "))

dollar_amount = euro_amount * exchange_rate

print("€", euro_amount, " = $", dollar_amount)
