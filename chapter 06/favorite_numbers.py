fav_num = {
        'matheus': [37, 70, 21],
        'vera': [65, 7],
        'peu': [99, 100, 0, 20],
        'sam': [101, 200],
        'maria': [86],
    }

for name, numbers in fav_num.items():
    print(f"\n{name.title()} favorite number(s):")
    for number in numbers:
        print(f"\t{number}")
