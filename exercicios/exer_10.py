'''Peça um número inteiro ao usuário.
● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima
cada número.'''
numero = int(input("Digite um número: "))

while numero >= 0:
    print(numero)
    numero -= 1