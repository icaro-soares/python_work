prompt = "\nHey, let's make a pizza!"
prompt += "\nTell me the ingredients, type 'quit' to exit: "
ingredient = ""
while True:
    ingredient = input(prompt).strip().lower()
    if ingredient == 'quit':
        break
    print(f"Adding some {ingredient}")
