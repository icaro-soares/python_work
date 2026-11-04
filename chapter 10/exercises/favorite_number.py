from pathlib import Path
import json


path = Path('chapter 10/exercises/favorite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It is {number}.")
else:
    while True:
        try:
            number = int(input("Which number is your favorite? "))
        except ValueError:
            print("Type a valid number!")
        else:
            contents = json.dumps(number)
            path.write_text(contents)
            print("Your secret is safe!")
            break
