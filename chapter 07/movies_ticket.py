while True:
    age = input("\nHow old are you (type 'quit' to exit? ")
    if age == 'quit':
        break
    age = int(age)
    print(f"You are {age} years old.")
    if age < 3:
        print("You don't have to pay for your ticket.")
    elif 3 <= age < 12:
        print("Your ticket costs U$S10 dollars.")
    else:
        print("Your ticket costs U$S15 dollars.")
print("Have a nice movie!")
