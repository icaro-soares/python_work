age = 20
stage = " "
print("The person is a(n) ", end='')
if age < 2:
    stage = "baby"
elif 2 <= age < 4:
    stage = "toddler" # usando pra descrever criança pequena
elif 4 <= age < 13:
    stage = "kid" # usando pra descrever criança em estágio adolescente
elif 13 <= age < 20:
    stage = "teenager" # usando pra descrever adolescente mais maduro
elif 20 <= age < 65:
    stage = "adult"
else:
    stage = "elder" # usando para descrever idoso (ancião lit.)
print(stage)
