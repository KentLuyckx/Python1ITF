animal_names = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("Original list:", "\t", animal_names)
help_variable = animal_names[0]
animal_names[0] = animal_names[-1]
animal_names[-1] = help_variable
print("After the switch", "\t", animal_names)
