lengte_in_km = 0.750
tijd_in_uur = 2/60
snelheid = lengte_in_km / tijd_in_uur
print("The gemiddelde snelheid van de Python is " + str(snelheid) + " km/u")


places_per_train = 28
trains_per_hour = 2
minutes_per_ride = 2
minutes_boarding_time = 0.5
capacity_per_hour = trains_per_hour * places_per_train * 60 / (minutes_boarding_time + minutes_per_ride)
print("The maximum capacity of the Python per hour is ", int(capacity_per_hour), " persons")

places_per_train = int(input("Enter the number of places per train"))
trains_per_hour = int(input("Input the number of trains per hour"))
minutes_per_ride = 2
minutes_boarding_time = 0.5
capacity_per_hour = trains_per_hour * places_per_train * 60 / (minutes_boarding_time + minutes_per_ride)
print("The maximum capacity of the Python per hour is ", int(capacity_per_hour), " persons")