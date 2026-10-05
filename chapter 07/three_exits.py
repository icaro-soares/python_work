prompt = "\nHey, let's make a pizza!"
prompt += "\nTell me the ingredients, type 'quit' to exit: "
# active = True
ingredient = ""
while True:
    ingredient = input(prompt).strip().lower()
    if ingredient == 'quit':
        print("Finishing your pizza...")
        break
    else:
        print(f"Adding some {ingredient}")
