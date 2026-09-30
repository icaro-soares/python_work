glossary = {
        'strings':'cadeia de caracteres',
        'int':'armazena valores numéricos inteiros',
        'float':'armazena valores numéricos com ponto flutuante',
        'boolean':'armazena apenas os valores True ou False',
        'tuples':'conjunto de itens que são imutáveis durante a execução do programa',
        'lists':'conjunto de itens que são mutáveis durante o programa',
        'dictionaries':'coleção de pares chave-valor',
        'loop':'estrutura usada para repetir um bloco escrevendo o código apenas uma vez',
        'if':'estrutura para testar condições lógicas',
        'comments':'notas de código ignoradas pelo interpretador'
    }


for k, v in glossary.items():
    print(f"{k.title()}:\n\t{v.capitalize()}")
