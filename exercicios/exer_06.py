'''Peça ao usuário um número inteiro.
● Use o operador de módulo (%) e uma estrutura if-else para determinar e imprimir se o
número é "par" ou "ímpar".'''
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número '{numero}' é par.")
else:
    print(f"O número '{numero}' é impar.")