try:
    x = input("First number: ")
    x = int(x)

    y = input("Second number: ")
    y = int(y)
except ValueError:
    print("Not a value!")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}")
