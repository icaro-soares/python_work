prompt = "\nTell me something and I'll tell you again."
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
