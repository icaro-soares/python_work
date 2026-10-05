prompt = "\nHey, let's make a pizza!"
prompt += "\nTell me the ingredients, type 'quit' to exit: "
ingredient = ""
while ingredient != 'quit':
    ingredient = input(prompt).strip().lower()
    if ingredient != 'quit':
        print(f"Adding some {ingredient}")
    else:
        print("Finishing your pizza...")
    