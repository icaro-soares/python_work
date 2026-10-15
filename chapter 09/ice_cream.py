class Restaurant:
    """Representa um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"Restaurant's name: {self.restaurant_name.title()}\nCuisine type: {self.cuisine_type.title()}")


    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "strawberry", "vanilla"]


    def show_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


my_restaurant = IceCreamStand("gelatteria", "gelatto")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.show_flavors()
