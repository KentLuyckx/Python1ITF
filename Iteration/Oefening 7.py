initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))

if initial_limit == final_limit:
    print("The sum of the numbers from", initial_limit, "till", final_limit)
    print(initial_limit)
elif initial_limit > final_limit:
    print("The initial limit must be smaller than the final limit!")
else:
    for counter in range(initial_limit, final_limit):
        initial_limit = initial_limit + (counter + 1)
        print("+", counter + 1, "=", initial_limit)
