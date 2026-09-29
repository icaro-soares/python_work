users = ['beca', 'tyler', 'admin', 'jason', 'morty']
for user in users:
    if user == 'admin':
        print("Hello administrator, would you like to see a status report?")
    else:
        print(f"Welcome {user.title()}, thanks for logging in again!")
