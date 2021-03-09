numbers_list = [9, 17, 25, 4, 12, 7]
print(numbers_list, "becomes ", end="")
even = sorted([i for i in numbers_list if i % 2 == 0])
uneven = sorted([i for i in numbers_list if i % 2 != 0])
print(even + uneven)
