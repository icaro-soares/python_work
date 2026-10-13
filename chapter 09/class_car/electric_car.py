from car import Car
from battery import Battery


class ElectricCar(Car):
    """Tentativa de representar um carro elétrico"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery()
