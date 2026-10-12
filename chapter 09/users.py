class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print("\nProfile info:")
        print(f"\t{self.first_name.title()}\n\t{self.last_name.title()}\n\t{self.age}\n\t{self.country.title()}")


user = User('hannah', 'montez', 32, 'mexico')
user2 = User('jonh', 'stone', 40, 'united states')
user3 = User('sasha', 'petrovic', 25, 'russia')

user.describe_user()
user2.describe_user()
user3.describe_user()
