user = input("Digite o usuario: ")
passwd = input("Digite a senha: ")

if((user == "well") & (passwd == "senha")):
    print(f'{user} logado com sucesso')
else:
    print("Infelizmente as credenciais não coincidem. Tente novamente.")
