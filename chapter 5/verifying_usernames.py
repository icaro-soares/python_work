current_users = ['perry', 'eilish', 'MOMOA', 'efron', 'diesel']
new_users = ['gaga', 'momoa', 'jackson', 'EFRON', 'rihanna']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} already taken!")
    else:
        print(f"{new_user} is available!")