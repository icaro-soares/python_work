from pathlib import Path
import json

path = Path('chapter 10/exercises/user_dict.json')

def get_stored_user_dict(path):
    """Loads user dict"""
    if path:
        contents = path.read_text()
        user_dict = json.loads(contents)
        print(f"Welcome back, {user_dict['username']}")
        for k, v in user_dict.items():
            print(f"\t{k}: {v}")
        return user_dict
    else:
        return None

def get_new_user_dict(path):
    """Get user info"""
    username = input("What's your username? ").title().strip()
    country = input("Which country where were you born? ").title().strip()
    age = int(input("How old are you? "))
    user_dict = {
            'username': username,
            'country': country,
            'age': age,
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    msg = f"We'll remember you when you come back, {user_dict['username']}"
    print(msg)
    return user_dict

def greet_user():
    """Greets the user"""
    if path.exists():
        user_dict = get_stored_user_dict(path)
    else:
        user_dict = get_new_user_dict(path)
    return user_dict
        

greet_user()
