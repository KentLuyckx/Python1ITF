with open('./files/weather_2018 08.csv') as file:
    next(file)  # Kan ook met line = file.readline() om de header weg te laten
    list_temperatures = []
    line = file.readline()
    while line:
        record = line.split(";")
        list_temperatures.append(record[1])
        line = file.readline()
print("The highest temperature in this period = {}°C".format(max(list_temperatures)))
