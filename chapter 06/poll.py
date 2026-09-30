favorite_languages = {
        'jen': 'python',
        'sarah':'c',
        'edward':'rust',
        'phil': 'python',
    }

should_in = ['hannah', 'mary', 'sarah', 'collins', 'phil']

for person in should_in:
    if person.lower() in set(favorite_languages.keys()):
        print(f"Thank you for answering our poll, {person.title()}")
    else:
        print(f"Hey, {person.title()}, please take our poll.")
