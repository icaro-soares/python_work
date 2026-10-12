class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name.title()}; its cuisine type is {self.cuisine_type.title()}")


    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


my_restaurant = Restaurant('oxente', 'nordestina')
your_restaurant = Restaurant('yon', 'oriental')
restaurant = Restaurant('poke', 'hawaiian')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
restaurant.describe_restaurant()
