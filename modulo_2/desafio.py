'''Desafio: Análise de Dados de Acessos

Sua tarefa é processar um fluxo de dados de acessos de usuários, identificando informações
importantes e tratando possíveis erros. O programa deve pedir ao usuário para inserir dados
de acesso, que consistem em um nome de usuário, um status de acesso e um número que
representa a duração da sessão em minutos.
O usuário pode inserir quantos acessos quiser. Para parar a inserção de dados, ele deve
digitar "parar".

Objetivo:
1. Armazene cada acesso válido como uma tupla (usuário, status, duracao_minutos).
2. Adicione essas tuplas a uma lista chamada registros_acessos.
3. Use um conjunto para armazenar todos os usuários que tiveram pelo menos um
acesso bem-sucedido.
4. No final, calcule e imprima o tempo total de todas as sessões bem-sucedidas.

Instruções:
● Use um laço while para continuar pedindo dados até que o usuário digite "parar".
● Para o status, ofereça um menu numérico com as opções 1 para "sucesso" e 2 para
"falha".
● Use condicionais para validar a entrada do menu (apenas 1 ou 2 são aceitos).
● Use um bloco try-except para garantir que a duração da sessão seja um número
válido. Se a conversão falhar, informe o usuário e descarte o registro, sem encerrar o
programa.
● Se o status for "sucesso", adicione o usuário ao seu conjunto de usuários
bem-sucedidos.'''

registros = []
usuarios_sucesso = set()
tempo = 0

while True:
    usuario = input("Digite o nome de usuário ou 'sair': ").lower()
    if usuario == "sair":
        break

    print("Selecione o seu status: \n01: Sucesso \n02: Falha")
    status = input("Sua opção: ")
    if status == "01":
        status_escolhido = "sucesso"
    elif status == "02":
        status_escolhido = "falha"
    else:
        print("Digite uma opção válida!")
        continue

    try:
        duracao = int(input("Digite a duração em minutos: "))
    except ValueError:
        print("Duração inválida!")
        continue

    acesso_lista = (usuario, status_escolhido, duracao)
    registros.append(acesso_lista)

    if status_escolhido == "sucesso":
        usuarios_sucesso.add(usuario)
        tempo += duracao
        print("Registro adicionado!")

print(f"Registros de acessos: {registros}")
print(f"Usuários com sucesso no acesso: {usuarios_sucesso}")
print(f"Tempo total das sessões bem sucessidas: {tempo} minutos")