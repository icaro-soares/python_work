numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if numbers:
    for n in numbers:
        print(n, end="")
        if n == 1:
            print("st")
        elif n == 2:
            print("nd")
        elif n == 3:
            print("rd")
        else:
            print("th")
