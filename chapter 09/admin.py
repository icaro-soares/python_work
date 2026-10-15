class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.country = country.title()
        self.login = 0


    def describe_user(self):
        print(f"User info:\n\t{self.first_name}\n\t{self.last_name}\n\t{self.age}\n\t{self.country}")


    def show_login_attempts(self):
        print(f"Login attempts: {self.login}")


    def login_attempts(self):
        self.login += 1


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user",]


    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, country,):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


my_user = Admin("ryan", "moses", 32, "belgium")
my_user.describe_user()
my_user.privileges.show_privileges()
