from pathlib import Path


try:
    path = Path('chapter 10/exercises/alice.txt')
except FileNotFoundError:
    print("File not found!")
else:
    content = path.read_text(encoding='utf-8')
    number = 0
    for line in content.splitlines():
        number += line.lower().count('alice')
    print(number)
    