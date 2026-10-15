class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.hodometer = 0


    def describe_car(self):
        print(f"{self.model} {self.make} {self.year}")


    def read_hodometer(self):
        print(f"This car has {self.hodometer} miles on it.")


    def update_hodometer(self, miles):
        if miles >= self.hodometer:
            self.hodometer = miles
        else:
            print("You can't roll back an hodometer!")

class Battery:
    pass


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 40


    def show_battery(self):
        print(f"This car has a {self.battery}-KWm battery.")


my_car = ElectricCar("nissan", "leaf", 2024)
my_car.read_hodometer()
my_car.update_hodometer(1000)
my_car.show_battery()
