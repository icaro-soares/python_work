from pathlib import Path
import json


def get_stored_username(path):
    """Gets the stored username, if available"""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_username(path):
    """Asks the username"""
    user = input("What's your username? ")
    contents = json.dumps(user)
    path.write_text(contents)
    return user


def greet_user():
    """Greets the user by its name"""
    path = Path('chapter 10/storing_data/username.json')
    user = get_stored_username(path)
    if user: # returns True
        print(f"Welcome back, {user.title()}!")
    else:
        user = get_new_username(path)
        print(f"We'll remember you when you come back, {user.title()}!")


greet_user()
