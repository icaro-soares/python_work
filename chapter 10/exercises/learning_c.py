from pathlib import Path


path = Path('chapter 10/exercises/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
    