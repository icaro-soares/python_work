dog = {
        'type': 'dog',
        'owner': 'mathaias',
}
cat = {
        'type': 'cat',
        'owner': 'sandra',
}
hamster = {
        'type': 'hamster',
        'owner': 'mike',
}
fish = {
        'type': 'fish',
        'owner': 'erica',
}
guinea_pig = {
        'type': 'guinea pig',
        'owner': 'max'
}
pets = [dog, cat, hamster, fish, guinea_pig]
for pet in pets:
    print(f"\nOwner: {pet['owner'].title()}\nType: {pet['type'].title()}")
