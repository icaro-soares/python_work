n = int(input('Número: '))
print(f"tabuada de {n}".upper().center(30))
print('-' * 30)
for c in range(1, 11):
    print(f'{c:2} x {n:2} = {c * n:3}'.center(30))
print('-' * 30)
