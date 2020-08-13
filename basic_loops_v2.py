r = range(21)

for num in r:
    if num:
        if num == 4 or num == 13:
            state = "unlucky"
        elif num % 2 == 0:
            state = "even"
        elif num % 2 != 0:
            state = "odd"
        print(f"{num} is {state}") 