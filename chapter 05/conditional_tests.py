mobile = 'iphone'
print(f"Are you using an iPhone or an Android?")
if mobile.lower() == 'iphone':
    print("Yes, it's an iPhone")
else:
    print(f"No, sorry. I'm using an Android device.")

device = 'samsung'
if device.lower() != 'samsung':
    print("You should try using an Android.")
else:
    print("Samsung is the best brand I've tried till now.")

x = 8
y = 10
print(f"X == Y? {x == y}")
print(f"X != Y? {x != y}")
print(f"X > Y? {x > y}")
print(f"X < Y? {x < y}")
