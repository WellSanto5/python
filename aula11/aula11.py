nome = input("Digite seu nome: ")

qtdCharacters = len(nome)

print(qtdCharacters)

if "/" in nome:
    print("Aqui nao cidadao")
else:
    print("Bem vindo")