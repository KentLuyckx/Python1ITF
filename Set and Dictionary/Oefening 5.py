months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
          'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

question = input('Please give a month (overview for overview)(enter for stop): ')

while question != '':
    if question == 'overview':
        for month in months:
            print(month, '\t', months[month])
    else:
        print(months.get(question, 'This month does not exist.'))
        # .get function allows you to catch errors with a message - separated by comma
        # in this case, if the 'key' from question variable is correct, it displays the value linked to key
        # if the key is not in dictionary - display the error message.
    question = input('Please give a month (overview for overview)(enter for stop): ')
