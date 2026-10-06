# Fazer com dicionários

places = []
visited_places = []
prompt = "If you could visit any place in the world "
prompt += "where would you go ('quit' to exit)? "
active = True

while active:
    answer = input(prompt)
    if answer != 'quit':
        places.append(answer)
    else:
        print("Poll finished.")
        active = False

while places:
    p = places.pop()
    visited_places.append(p)
visited_places.sort()

print("\nVisited places:")
for i, place in enumerate(visited_places):
    print(f"{i:<3}{place:>20}")
