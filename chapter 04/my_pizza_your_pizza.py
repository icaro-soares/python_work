pizzas = ['mussarela', 'calabresa', 'portuguesa']
friends_pizzas = pizzas[:]
pizzas.append('charque')
friends_pizzas.append('napolitano')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza.title()}")

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"\t{pizza.title()}")
    