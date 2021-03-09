def dollar(euro_amount, rate):
    return euro_amount * rate


exchange_rate = float(input("Current dollar rate (€ -> $): "))
euro = float(input("Your amount in euro: "))

# possible print 1
# print("€", euro, " = $", dollar(euro, exchange_rate))

# possible print 2
print("€ {} = $ {}".format(euro, dollar(euro, exchange_rate)))
