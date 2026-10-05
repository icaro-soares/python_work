sandwich_orders = ["americano", "misto", "x-egg", "x-bacon", "vegetariano"]
finished_sandwiches = []
while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(f"Seu sanduíche {sandwich.title()} está pronto.")
