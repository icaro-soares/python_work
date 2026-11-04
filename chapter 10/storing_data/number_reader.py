from pathlib import Path
import json


path = Path('chapter 10/storing_data/numbers.json') # path do arquivo .json
contents = path.read_text() # abre o arquivo para leitura
numbers = json.loads(contents) # informa ao json para carregar o arquivo
print(numbers) # imprime os dados na tela
