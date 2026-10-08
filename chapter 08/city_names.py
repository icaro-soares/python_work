def city_country(city, country="brazil"):
    phrase = f"{city.title()}, {country.title()}"
    return phrase


country0 = city_country("paris", "france")
print(country0)
country1 = city_country(country="phillipines", city="pattaya")
print(country1)
country2 = city_country("new jersey", "united states")
print(country2)
