class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}, its cuisine is {self.cuisine_type.title()}.")


    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


    def show_number_served(self):
        print(f"Clients served: {self.number_served}")


    def set_number_served(self, value):
        self.number_served = value


    def increment_number_served(self, value):
        self.number_served += value


my_restaurant = Restaurant('poke', 'hawaiian food')
my_restaurant.show_number_served()
#my_restaurant.number_served = 10
#my_restaurant.show_number_served()
#my_restaurant.set_number_served(23)
#my_restaurant.show_number_served()
my_restaurant.increment_number_served(45)
my_restaurant.show_number_served()
