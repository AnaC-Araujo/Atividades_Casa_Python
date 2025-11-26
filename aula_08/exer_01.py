senha_correta = "administrador123"

while True:
    senha_fornecida = input("Senha: ")
    if senha_fornecida == senha_correta:
        print("Login liberado!")
        break
    else:
        print("Informe a senha correta.!")

'''while True:'''
continuar = True
while continuar:
    email_fornecido = input("Digite um e-mail para validação: ")
    if "@" in email_fornecido and email_fornecido.endswith(".com"):
        print("E-mail válido!")
        break
    else:
        print("E-mail inválido!")

pergunta = input("Deseja validar outro e-mail? 1- Sim ou 2-Não ")
while True:
    if pergunta == "1":
        email_fornecido_2 = input("Digite um e-mail para validação: ")
        verificacao_2 = email_fornecido_2.endswith(".com")
        if "@" in email_fornecido_2 and verificacao_2:
            print("E-mail válido!")
            break
        else:
            print("E-mail inválido!")
    else:
        print("Encerrando validação de e-mail.")
        break