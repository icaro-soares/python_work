prompt = "\nHey, let's make a pizza!"
prompt += "\nTell me the ingredients, type 'quit' to exit: "
active = True
ingredient = ""
while active:
    ingredient = input(prompt).strip().lower()
    if ingredient == 'quit':
        active = False
        print("Finishing your pizza...")
    else:
        print(f"Adding some {ingredient}")
