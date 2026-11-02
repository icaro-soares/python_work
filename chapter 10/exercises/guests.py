from pathlib import Path


path = Path('chapter 10/exercises/guest.txt')

name = input("What's your name? ").title().strip()
path.write_text(name)
