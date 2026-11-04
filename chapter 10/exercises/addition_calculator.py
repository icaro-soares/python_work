while True:
    try:
        x = input("First number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Second number: ")
        if x == 'q':
            break
        y = int(y)
    except ValueError:
        print("Not a number!")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}")
