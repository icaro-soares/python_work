sandwich_orders = ["americano", "x-tudo", "vegano"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(new_sandwich)
    print(f"Your {new_sandwich.title()} sandwich is ready.")
