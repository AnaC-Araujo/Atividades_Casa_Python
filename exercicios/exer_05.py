'''Peça ao usuário para digitar dois números inteiros.
● Use if-else para descobrir qual dos dois é o maior e imprima o resultado.'''
numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
if numero_1 > numero_2:
    print(f"O número '{numero_1}' é maior.")
else:
    print(f"O número '{numero_2}' é maior.")