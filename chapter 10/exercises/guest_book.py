from pathlib import Path


path = Path('chapter 10/exercises/guest_book.txt')

guest_list = []

while True:
    guest = input("What's your name? ")
    if guest == 'quit':
        break
    guest_list.append(guest)
    print("Thank you for joining us!")

file_string = ''
for guest in guest_list:
    file_string += f"{guest}\n"
    
path.write_text(file_string)
