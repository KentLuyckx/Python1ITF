first_names_1ITF = set(open('./files/first_names1ITF.txt').read().split())
# Open, read, and strip white spaces from file

print('In 1ITF there are', len(first_names_1ITF), 'different first names.')
# Set length = number of names - no need for a loop

first_names_2ITF = set(open('./files/first_names2ITF.txt').read().split())
# Open, read, and strip white spaces from file

print('In 2ITF there are', len(first_names_2ITF), 'different first names.')
# Set length = number of names - no need for a loop

first_names_total = first_names_1ITF.intersection(first_names_2ITF)
# Intersection looks for the same values. If names match, we put them in a new set

print('These are the', len(first_names_total), 'first names appearing in both 1ITF and 2ITF')
# Length of set = number of names

for name in sorted(first_names_total):
    # Sorted forces collection data types into a list type
    print(name)
    # Print the list entries one by one

first_names_1ITF.close()
first_names_2ITF.close()