my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

friends_food.append('ice cream')
print("My favorite food:")
for food in my_foods:
    print(f"\t{food.title()}")
print("My friend's favorite food:")
for food in friends_food:
    print(f"\t{food.title()}")
    