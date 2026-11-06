from city_functions import city_country


def test_city_country():
    """Tests if the function works properly"""
    formatted_name = city_country('osaka', 'japan')
    assert formatted_name
