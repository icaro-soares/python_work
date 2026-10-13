class Battery:
    """Representa a bateria de um carro elétrico"""
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    
    def describe_battery(self):
        """Exibe uma mensagem exibindo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-KWh battery.") 


    def fill_gas_tank(self):
        """Exibe uma mensagem que não precisa encher o tanque"""
        print("Electric cars don't have gas tank!")


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
