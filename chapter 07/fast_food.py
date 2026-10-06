sandwich_orders = ["misto", "americano", "x-egg", "x-bacon"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Seu pedido {sandwich.title()} está pronto!")
    finished_sandwiches.append(sandwich)
print("\nOs seguintes sanduíches foram preparados:")
for indice, sandwich in enumerate(sorted(finished_sandwiches)):
    print(f"{indice:<5}{sandwich:>10}")
