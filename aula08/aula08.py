nome = "Wellington"
idade = 20
altura = 1.73
peso = 65.5
anoAtual = 2022
anoNascimento = anoAtual - idade 
imc = peso / altura ** 2

print(f'Ola {nome}, sua idade é {idade} pois você nasceu no ano de {anoNascimento}. Seu imc é de {imc:.2f}')