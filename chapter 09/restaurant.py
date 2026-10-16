class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}; its cuisine is {self.cuisine_type.title()}")


    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
