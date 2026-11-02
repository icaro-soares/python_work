from pathlib import Path


path = Path('chapter 10/exercises/guest_book.txt')

guest_names = []

while True:
    name = input("What's your name (quit stop)? ").lower().strip()
    if name == 'quit':
        break
    print(f"Thanks for coming {name.title()}")
    guest_names.append(name)  

file_string = ''
for guest in guest_names:
    file_string += f"{guest.title()}\n"

path.write_text(file_string)
