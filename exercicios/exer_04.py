'''● Defina uma senha secreta em uma variável (str, por exemplo, "python123").
● Peça ao usuário para digitar uma senha.
● Use if-else para verificar se a senha digitada é igual à senha secreta. Imprima "Acesso
concedido" ou "Senha incorreta".'''

senha_secreta = "adm123"
senha = input("Digite sua senha: ")
if senha == senha_secreta:
    print("Acesso liberado.")
else:
    print("Senha incorreta")