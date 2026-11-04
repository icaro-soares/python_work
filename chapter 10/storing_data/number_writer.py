from pathlib import Path
import json


numbers = [n**2 for n in range(1, 11, 2)]

path = Path('chapter 10/storing_data/numbers.json') # path do arquivo criado
contents = json.dumps(numbers) # armazena a lista 'numbers' no arquivo criado
path.write_text(contents) # escreve a lista armazena no arquivo para leitura
