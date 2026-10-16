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


    def update_hodometer(self, value):
        if value >= self.hodometer:
            self.hodometer += value
        else:
            print("You can't roll back an hodometer!")


    def increment_hodometer(self, value):
        self.hodometer += value
        

class Battery:
    def __init__(self, battery_capacity=40):
        self.battery = battery_capacity


    def show_battery(self):
            print(f"This car has a {self.battery}-KWm battery.")


    def get_range(self):
        if self.battery == 40:
            range = 150
        else:
            range = 225
        print(f"This car can go about {range} miles on full charge.")


    def upgrade_battery(self, value=65):
        self.battery = value


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
my_leaf.describe_car()
my_leaf.read_hodometer()
my_leaf.increment_hodometer(200)
my_leaf.read_hodometer()
my_leaf.update_hodometer(100)
my_leaf.read_hodometer()
my_leaf.increment_hodometer(300)
my_leaf.read_hodometer()
my_leaf.battery.show_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.show_battery()
my_leaf.battery.get_range()
