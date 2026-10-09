def make_car(fabricante, model, **kwargs):
    kwargs['fabricante'] = fabricante
    kwargs['model'] = model
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('gol', 'volkswagem', color='silver')
car3 = make_car('ferrari', 'ferrari', color='red', air_conditioning=True, airbags=True)
print(car)
print(car2)
print(car3)
