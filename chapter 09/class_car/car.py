class Car:
    """Representação de um carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0


    def get_descriptive_name(self):
        """Retorna os dados do carro de maneira elegante"""
        print(f"{self.year} {self.make.title()} {self.model.title()}")


    def read_odometer(self):
        """Retorna a leitura do hodometro"""
        print(f"This car has {self.odometer} miles on it.")


    def update_odometer(self, value):
        """Atualiza o valor do hodometro se o valor for maior ou igual"""
        if value >= self.odometer:
            self.odometer = value
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, value):
        """Incrementa o valor do hodometro"""
        self.odometer += value


    def fill_gas_tank(self):
        """Exibe mensagem pedindo para encher o tanque"""
        print("You have to fill your gas tank!")
