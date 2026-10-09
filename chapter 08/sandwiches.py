def make_sandwich(*ingredients):
    print("\nMaking sandwich")
    for i in ingredients:
        print(f"\t{i.title()}")


make_sandwich('ham')
make_sandwich('lettuce', 'fried chicken', 'eggs')
make_sandwich('tuna', 'extra cheese')
