users = []
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello administrator, would you like to see a status report?")
        else:
            print(f"Thanks for logging in again, {user.title()}!")
else:
    print("We must find some users!")
