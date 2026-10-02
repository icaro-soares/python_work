favorite_places = {
        'hannah': ['paris'],
        'maria': ['london', 'egypt', 'china'],
        'peter': ['greece', 'austria'],
        }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"\t{place.title()}")
