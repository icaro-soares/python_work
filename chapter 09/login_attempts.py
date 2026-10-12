class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0


    def describe_user(self):
        print("\nProfile info:")
        print(f"\t{self.first_name.title()}\n\t{self.last_name.title()}\n\t{self.age}\n\t{self.country.title()}")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


    def show_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")

user = User('hannah', 'montez', 30, 'mexico')
user.describe_user()
user.show_login_attempts()
user.increment_login_attempts()
user.show_login_attempts()
user.reset_login_attempts()
user.show_login_attempts()
