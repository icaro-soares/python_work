ana = {
        'first_name': 'ana',
        'last_name': 'calaça',
        'age': 42,
        'city': 'belgium',
}
leo = {
        'first_name': 'leo',
        'last_name': 'santos',
        'age': 35,
        'city': 'rio de janeiro',
}
cathy = {
        'first_name': 'cathy',
        'last_name': 'moon',
        'age': 24,
        'city': 'beverly hills',
}
people = [ana, leo, cathy]
for person in people:
    print(f"Full name: {person['first_name'].title()} {person['last_name'].title()}\nAge: {person['age']}\nCity: {person['city'].title()}")
    print('-='*30)
