from pathlib import Path


path = Path('chapter 10/exercises/learning_python.txt')
content = path.read_text()
for line in content.splitlines():
    print(line)
    