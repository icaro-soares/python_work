def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        sent = messages.pop()
        print(f"Sending message [{sent}]...")
        sent_messages.append(sent)


messages = ["hello", "ciao", "bonjour"]
sent_messages = []
#show_messages(messages)
send_messages(messages, sent_messages)
print(f"Messages: {messages}")
print(f"Sent_messages: {sent_messages}")
