def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        sending = messages.pop()
        print(f"Sending message [{sending}]")
        sent_messages.append(sending)


messages = ["olá", "ciao", "bonjour"]
sent_messages = []
send_messages(messages[:], sent_messages)
print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")
