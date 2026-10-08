# Fazer com dicionários
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("Which place would you go on vacation? ")

    responses[name] = place

    c = input("Would you like to continue? (y/n) ")
    if c == 'n':
        print("\nThank you!\n")
        polling_active = False

for k, v in responses.items():
    print(f"{k.title()} would go to {v.title()} in vacation.")
