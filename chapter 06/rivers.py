rivers = {
        'nile':'egypt',
        'reno':'france',
        'amazonas':'brazil',
    }


for river, country in rivers.items():
    print(f"The {river.title()} crosses {country.title()}")
print()
for river in rivers.keys():
    print(f"{river.title()}")
print()
for country in rivers.values():
    print(f"{country.title()}")
