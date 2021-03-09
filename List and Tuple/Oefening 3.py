animal_names = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("Original list:", "\t", animal_names)
start = animal_names[0]  # Save cat into a help variable
animal_names.remove(animal_names[0])  # Remove cat from the original list
animal_names.append(start)  # Add cat to the end of the list
print("After sliding:", "\t", animal_names)