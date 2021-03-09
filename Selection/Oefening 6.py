is_morning = bool(0)
is_mother = bool(0)
is_sleeping = bool(0)

if is_sleeping is True:
    print("I'm not answering my phone.")
elif is_morning is True and is_mother is False:
    print("I'm not answering my phone.")
elif is_morning is True and is_mother is True:
    print('Hi mom.')
elif is_morning is False:
    print('Hello.')
