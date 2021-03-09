def fahrenheit(degrees_celsius):
    return degrees_celsius * 9/5 + 32


celsius = float(input("Degrees Celsius: "))
print("{:.2f}".format(celsius), "degrees Celsius =", "{:.2f}".format(fahrenheit(celsius)), "degrees Fahrenheit")
