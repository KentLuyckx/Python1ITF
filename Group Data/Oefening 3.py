print('Average temperatures:')

with open('./files/weather_2018 10.csv') as file:
    next(file)
    line = file.readline().rstrip()
    measurement = line.split(';')

    while line:
        # date_list = measurement[0].split(' ')
        # date = date_list[0]
        date = measurement[0].split(' ')[0]  # Single line of above comments
        measurement_counter = 0
        temperature_total = 0

        while line and date == measurement[0].split(' ')[0]:
            measurement_counter += 1
            temperature_total += float(measurement[1])  # Cast to float for safety
            line = file.readline().rstrip()
            measurement = line.split(';')

        average_temperature = temperature_total / measurement_counter

        # :.4 to show 4 digits, 2 whole numbers and 2 after comma for average temperature
        print('{}\tnumber of measurements = {}\taverage = {:.4}'.format(date, measurement_counter, average_temperature))
