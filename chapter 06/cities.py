cities = {
        'recife': {
                'country': 'brazil',
                'population': 1_588_983,
                'fact': 'Well known as Brazilian Venice',
                },
        'new york': {
                'country': 'united states of america',
                'population': 8_000_000,
                'fact': 'The city that never sleeps',
                },
        'paris': {
                'country': 'france',
                'population': 2_100_000,
                'fact': 'Well known as The City of Lights',
                }
        }

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    curious_fact = city_info['fact']
    print(f"\nCity: {city.title()}\n\tCountry: {country}\n\tPopulation: {population}\n\tCurious fact: {curious_fact}")
