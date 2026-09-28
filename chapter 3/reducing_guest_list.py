guests = ['barack obama', 'nelson mandela', 'juscelino kubistchek', 'george bush', 'viola davis', 'kamala harris']
print("Sorry, we can't afford to have too many guests, only two of them will come to our dinner")
last_guest = guests.pop()
print(f"Sorry, {last_guest.title()}, you're uninvited")
last_guest = guests.pop()
print(f"Sorry, {last_guest.title()}, you're uninvited")
last_guest = guests.pop()
print(f"Sorry, {last_guest.title()}, you're uninvited")
last_guest = guests.pop()
print(f"Sorry, {last_guest.title()}, you're uninvited")
del guests[0]
del guests[0]
print(guests)
