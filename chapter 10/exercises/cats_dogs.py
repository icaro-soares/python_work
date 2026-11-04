from pathlib import Path

filenames = [
        'chapter 10/exercises/cats.txt',
        'chapter 10/exercises/dogs.txt',
]

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {filename} does not exist!")
    else:
        print(contents.title())
